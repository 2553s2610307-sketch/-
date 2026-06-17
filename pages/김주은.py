import streamlit as st
import random

st.set_page_config(
    page_title="AI 맞춤형 도서 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI 맞춤형 도서 추천기")
st.write("관심 분야와 취향을 선택하면 맞춤형 도서를 추천합니다.")

# 도서 데이터베이스
books = [
    {
        "title": "사피엔스",
        "author": "유발 하라리",
        "field": "역사",
        "purpose": "교양",
        "level": "보통"
    },
    {
        "title": "코스모스",
        "author": "칼 세이건",
        "field": "과학",
        "purpose": "교양",
        "level": "보통"
    },
    {
        "title": "아주 작은 습관의 힘",
        "author": "제임스 클리어",
        "field": "자기계발",
        "purpose": "성장",
        "level": "쉬움"
    },
    {
        "title": "딥 워크",
        "author": "칼 뉴포트",
        "field": "자기계발",
        "purpose": "성장",
        "level": "어려움"
    },
    {
        "title": "1984",
        "author": "조지 오웰",
        "field": "소설",
        "purpose": "재미",
        "level": "보통"
    },
    {
        "title": "데미안",
        "author": "헤르만 헤세",
        "field": "소설",
        "purpose": "성찰",
        "level": "보통"
    },
    {
        "title": "이기적 유전자",
        "author": "리처드 도킨스",
        "field": "과학",
        "purpose": "학습",
        "level": "어려움"
    },
    {
        "title": "그릿",
        "author": "앤절라 더크워스",
        "field": "자기계발",
        "purpose": "성장",
        "level": "보통"
    }
]

# 사용자 입력
field = st.selectbox(
    "관심 분야",
    ["소설", "과학", "역사", "자기계발"]
)

purpose = st.selectbox(
    "독서 목적",
    ["재미", "성장", "교양", "학습", "성찰"]
)

level = st.selectbox(
    "선호 난이도",
    ["쉬움", "보통", "어려움"]
)

# 추천 버튼
if st.button("📖 책 추천받기"):

    recommendations = [
        book for book in books
        if book["field"] == field
        and book["purpose"] == purpose
        and book["level"] == level
    ]

    # 조건이 너무 좁을 경우
    if len(recommendations) == 0:
        recommendations = [
            book for book in books
            if book["field"] == field
        ]

    if recommendations:
        book = random.choice(recommendations)

        st.success("추천 도서가 선정되었습니다!")

        st.markdown(f"""
        ### 📚 {book['title']}
        **저자:** {book['author']}

        **관심 분야:** {book['field']}
        
        **독서 목적:** {book['purpose']}
        
        **난이도:** {book['level']}
        """)

    else:
        st.warning("조건에 맞는 책이 없습니다.")
