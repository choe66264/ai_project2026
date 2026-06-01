import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="커피판매점 연도별 분석", layout="wide")

st.title("☕ 커피판매점 연도별 분석")

files = st.file_uploader(
    "연도별 CSV 파일을 여러 개 업로드하세요",
    type="csv",
    accept_multiple_files=True
)

if files:

    data = []

    for file in files:

        try:
            df = pd.read_csv(file, encoding="cp949")
        except:
            file.seek(0)
            df = pd.read_csv(file, encoding="utf-8")

        # 파일명 예시: coffe_2023.csv
        year = ''.join(filter(str.isdigit, file.name))[:4]

        data.append({
            "연도": int(year),
            "판매점수": len(df)
        })

    result = pd.DataFrame(data)

    top5 = result.sort_values(
        "판매점수",
        ascending=False
    ).head(5)

    st.subheader("판매점 수 TOP 5 연도")
    st.dataframe(top5, use_container_width=True)

    # Folium 지도
    m = folium.Map(
        location=[35.10, 129.02],
        zoom_start=11
    )

    for i, row in top5.reset_index().iterrows():

        folium.Marker(
            location=[
                35.10 + i * 0.01,
                129.02 + i * 0.01
            ],
            popup=f"{row['연도']}년 : {row['판매점수']}개"
        ).add_to(m)

    st.subheader("Folium 지도")
    st_folium(m, width=1000, height=600)

    st.subheader("막대그래프")

    st.bar_chart(
        top5.set_index("연도")["판매점수"]
    )
