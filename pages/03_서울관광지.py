": 126.988227,import streamlit as st
        "name": "이태원",
        "lat": 37.534925,
        "lon": 126.994684,
        "subway": "이태원역",
        "fun": "세계 음식 탐방, 펍 투어"
    },
    {
        "name": "DDP",
        "lat": 37.566525,
        "lon": 127.009223,
        "subway": "동대문역사문화공원역",
        "fun": "야간 조명 감상, 전시회 관람"
    }
]

# 기본 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 추가
for place in places:
    popup_text = f"""
    <b>{place['name']}</b><br>
    클릭해서 아래 상세정보 확인
    """

    folium.Marker(
        location=[place['lat'], place['lon']],
        popup=popup_text,
        tooltip=place['name'],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_data = st_folium(m, width=1200, height=600)

st.divider()

# 클릭된 장소 정보 표시
clicked = map_data.get("last_object_clicked_popup")

if clicked:
    selected_place = None

    for place in places:
        if place['name'] in clicked:
            selected_place = place
            break

    if selected_place:
        st.subheader(f"📍 {selected_place['name']}")
        st.success(
            f"🚇 가까운 지하철역: {selected_place['subway']} | 🎉 놀거리: {selected_place['fun']}"
        )
else:
    st.info("지도에서 관광지를 클릭해보세요!")

# 하단 관광지 목록
