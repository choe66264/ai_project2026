from pathlib import Path
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="커피판매점 지도",
    layout="wide"
)

st.title("☕ 부산 서구 커피판매점 현황")

# CSV 경로
csv_path = Path(__file__).parent.parent / "coffe.csv"

# 데이터 읽기
try:
    df = pd.read_csv(csv_path, encoding="cp949")
except:
    df = pd.read_csv(csv_path, encoding="utf-8")

st.success(f"총 판매점 수 : {len(df)}개")

st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 부산 서구 중심 좌표
center_lat = 35.097
center_lon = 129.024

m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=13
)

# 주소 컬럼 찾기
address_col = None

for col in df.columns:
    if "소재지" in col or "주소" in col:
        address_col = col
        break

# 위치 정보가 없으므로 예시 마커 생성
for idx, row in df.head(50).iterrows():

    lat = center_lat + (idx % 10) * 0.001
    lon = center_lon + (idx % 10) * 0.001

    popup_text = ""

    if "업소명" in df.columns:
        popup_text += f"업소명 : {row['업소명']}<br>"

    if address_col:
        popup_text += f"주소 : {row[address_col]}"

    folium.Marker(
        location=[lat, lon],
        popup=popup_text
    ).add_to(m)

st.subheader("🗺️ 커피판매점 지도")

st_folium(
    m,
    width=1000,
    height=600
)

st.subheader("📊 판매점 수")

count_df = pd.DataFrame({
    "구분": ["커피판매점"],
    "개수": [len(df)]
})

st.bar_chart(
    count_df.set_index("구분")
)
