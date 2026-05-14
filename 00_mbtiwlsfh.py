import streamlit as st

# MBTI별 진로 데이터
career_data = {
    "INTJ": [
        {
            "job": "데이터 분석가",
            "major": "컴퓨터공학과, 데이터사이언스학과",
            "personality": "논리적이고 분석적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "연구원",
            "major": "자연과학계열, 공학계열",
            "personality": "탐구심이 강하고 집중력이 높은 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "INTP": [
        {
            "job": "프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "창의적이고 문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "대학교수",
            "major": "교육학과, 전공 관련 학과",
            "personality": "지식을 탐구하고 설명하는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ENTJ": [
        {
            "job": "기업 경영인",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표지향적인 사람",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "job": "마케팅 매니저",
            "major": "마케팅학과, 광고홍보학과",
            "personality": "전략적 사고와 추진력이 좋은 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ENTP": [
        {
            "job": "광고 기획자",
            "major": "광고홍보학과",
            "personality": "아이디어가 많고 도전을 좋아하는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "창업가",
            "major": "경영학과",
            "personality": "새로운 시도를 즐기는 사람",
            "salary": "평균 연봉 약 6,000만원 이상"
        }
    ],
    "INFJ": [
        {
            "job": "상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "작가",
            "major": "문예창작학과",
            "personality": "상상력과 감수성이 풍부한 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],
    "INFP": [
        {
            "job": "디자이너",
            "major": "시각디자인학과",
            "personality": "감성이 풍부하고 창의적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "작곡가",
            "major": "실용음악과",
            "personality": "예술적 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],
    "ENFJ": [
        {
            "job": "교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "인사 담당자",
            "major": "경영학과",
            "personality": "소통 능력이 좋은 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ENFP": [
        {
            "job": "유튜버",
            "major": "미디어학과",
            "personality": "활발하고 표현력이 좋은 사람",
            "salary": "평균 연봉 수입 편차 큼"
        },
        {
            "job": "행사 기획자",
            "major": "이벤트학과, 관광학과",
            "personality": "사교적이고 창의적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ISTJ": [
        {
            "job": "회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감이 강한 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "공무원",
            "major": "행정학과",
            "personality": "성실하고 안정적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ISFJ": [
        {
            "job": "간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 책임감 있는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "사회복지사",
            "major": "사회복지학과",
            "personality": "남을 돕는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],
    "ESTJ": [
        {
            "job": "경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "관리자",
            "major": "경영학과",
            "personality": "체계적이고 리더십 있는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ESFJ": [
        {
            "job": "승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ISTP": [
        {
            "job": "자동차 정비사",
            "major": "자동차공학과",
            "personality": "손재주가 좋고 실용적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 집중력이 높은 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "ISFP": [
        {
            "job": "플로리스트",
            "major": "원예학과",
            "personality": "감각적이고 섬세한 사람",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "셰프",
            "major": "조리학과",
            "personality": "창의성과 손재주가 좋은 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ESTP": [
        {
            "job": "영업 전문가",
            "major": "경영학과",
            "personality": "도전적이고 활동적인 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "스포츠 코치",
            "major": "체육학과",
            "personality": "에너지가 넘치고 적극적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ESFP": [
        {
            "job": "배우",
            "major": "연극영화과",
            "personality": "사람들 앞에 나서는 것을 좋아하는 사람",
            "salary": "평균 연봉 수입 편차 큼"
        },
        {
            "job": "바리스타",
            "major": "카페경영과, 호텔조리학과",
            "personality": "사교적이고 분위기를 잘 만드는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ]
}

st.set_page_config(page_title="MBTI 진로 추천", page_icon="✨")

st.title("✨ MBTI 기반 진로 추천 프로그램")
st.write("MBTI를 선택하면 추천 진로 2가지를 알려드립니다!")

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(career_data.keys())
)

if st.button("진로 추천 보기"):
    st.subheader(f"{mbti} 유형 추천 진로")

    careers = career_data[mbti]

    for idx, career in enumerate(careers, start=1):
        st.markdown(f"## {idx}. {career['job']}")
        st.write(f"📚 적합한 학과: {career['major']}")
        st.write(f"🧑 성격 특징: {career['personality']}")
        st.write(f"💰 {career['salary']}")
        st.divider()

st.caption("※ 연봉은 평균적인 예시이며 실제와 차이가 있을 수 있습니다.")
