import streamlit as st
import random

# 기본 메뉴 데이터
menu_data = {
    "한식": ["비빔밥", "된장찌개", "김치찌개", "불고기", "제육볶음", "냉면", "칼국수"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부", "볶음밥"],
    "일식": ["초밥", "돈카츠", "우동", "라멘", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "샐러드"],
    "기타": ["샌드위치", "도시락", "분식", "김밥", "떡볶이"]
}

st.title("🤔 점심 뭐 먹지?")

# 카테고리 선택
selected_categories = st.multiselect(
    "먹고 싶은 메뉴 카테고리를 골라보세요:",
    options=list(menu_data.keys()),
    default=list(menu_data.keys())
)

# 추천 버튼
if st.button("🍱 메뉴 추천 받기!"):
    # 선택된 카테고리에서 메뉴 리스트 뽑기
    candidate_menu = []
    for cat in selected_categories:
        candidate_menu.extend(menu_data[cat])
    
    if candidate_menu:
        menu = random.choice(candidate_menu)
        st.success(f"오늘의 추천 메뉴는 👉 **{menu}** 입니다!")
    else:
        st.warning("카테고리를 하나 이상 선택해주세요!")

# 옵션: 메뉴 직접 추가
with st.expander("✏️ 내가 메뉴를 추가하고 싶다면?"):
    new_category = st.selectbox("카테고리 선택", list(menu_data.keys()))
    new_menu = st.text_input("추가할 메뉴 이름을 입력하세요:")
    if st.button("➕ 메뉴 추가"):
        if new_menu:
            menu_data[new_category].append(new_menu)
            st.success(f"{new_category}에 **{new_menu}** 추가 완료!")
        else:
            st.error("메뉴 이름을 입력해주세요.")
