# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(page_title="서울시 행정구별 인구수", layout="wide")

st.title("서울시 행정구별 인구수")

# ---------------------------
# 한글 폰트 설정
# ---------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ---------------------------
# 데이터 불러오기
# ---------------------------
df = pd.read_csv("population.csv", encoding="cp949")

# 컬럼 이름 공백 제거
df.columns = df.columns.str.strip()

# 첫 번째 컬럼 이름 확인
district_col = df.columns[0]

# 행정구 목록
districts = df[district_col].tolist()

# 선택 박스
selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택된 행 데이터
selected_row = df[df[district_col] == selected_district].iloc[0]

# ---------------------------
# 연령 컬럼 추출
# ---------------------------
age_columns = []

for col in df.columns:
    if "세" in col or "이상" in col:
        age_columns.append(col)

# 숫자 데이터만 추출
population_values = []

for col in age_columns:
    try:
        value = str(selected_row[col]).replace(",", "")
        population_values.append(int(value))
    except:
        population_values.append(0)

# ---------------------------
# 그래프 생성
# ---------------------------
fig, ax = plt.subplots(figsize=(14, 6))

# 회색 배경
fig.patch.set_facecolor('lightgray')
ax.set_facecolor('lightgray')

# 빨간색 꺾은선 그래프
ax.plot(
    age_columns,
    population_values,
    color='red',
    linewidth=2,
    marker='o'
)

# 제목
ax.set_title(
    "서울시 행정구별 인구수",
    fontsize=18,
    fontweight='bold'
)

# 축 제목
ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# x축 글자 회전
plt.xticks(rotation=70)

# 격자
ax.grid(True)

# Streamlit 출력
st.pyplot(fig)
