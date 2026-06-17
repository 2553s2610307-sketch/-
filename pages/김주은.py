import streamlit as st
import random

st.set_page_config(
    page_title="BookMatch",
    page_icon="📚",
    layout="centered"
)

BOOK_DB = {
    "IT·프로그래밍": [
        {
            "title": "혼자 공부하는 파이썬",
            "level": "입문",
            "reason": "파이썬을 처음 배우는 사람에게 적합"
        },
        {
            "title": "클린 코드",
            "level": "중급",
            "reason": "좋은 코드 작성 습관을 배우기 좋음"
        },
        {
            "title": "데이터 중심 애플리케이션 설계",
            "level": "고급",
            "reason": "대규모 시스템 설계 학습에 적합"
        }
    ],
    "인공지능": [
        {
            "title": "밑바닥부터 시작하는 딥러닝",
            "level": "입문",
            "reason": "딥러닝 개념을 쉽게 설명"
        },
        {
            "title": "핸즈온 머신러닝",
            "level": "중급",
            "reason": "실습 중심 학습 가능"
        },
        {
            "title": "패턴 인식과 머신러닝",
            "level": "고급",
            "reason": "이론을 깊이 있게 학습 가능"
        }
    ],
    "자기계발": [
        {
            "title": "아주 작은 습관의 힘",
            "level": "입문",
            "reason": "습관 형성에 대한 실용적 조언"
        },
        {
            "title": "딥 워크",
            "level": "중급",
            "reason": "집중력 향상 전략 제시"
        }
    ],
    "경제·투자": [
        {
            "title": "돈의 심리학",
            "level": "입문",
            "reason": "돈과 투자에 대한 사고방식 이해"
        },
        {
            "title": "현명한 투자자",
            "level": "고급",
            "reason": "가치투자의 고전"
        }
    ],
    "심리학": [
        {
            "title": "생각에 관한 생각",
            "level": "중급",
            "reason": "인간의 의사결정 원리 이해"
        }
    ],
    "역사": [
        {
            "title": "총 균 쇠",
            "level": "중급",
            "reason": "인류 문명의 발전 과정 설명"
        }
    ],
    "과학": [
        {
            "title": "코스모스",
            "level": "입문",
            "reason": "과학의 아름다움을 쉽게 전달"
        }
    ],
    "소설": [
        {
            "title": "데미안",
            "level": "입문",
            "reason": "성장과 자아 탐색의 고전"
        }
    ],
    "철학": [
        {
            "title": "정의란 무엇인가",
            "level": "입문",
            "reason": "철학적 사고 입문서"
        }
    ]
}


def recommend_books(category, level):
    books = BOOK_DB.get(category, [])

    if not books:
        return []

    matched = [book for book in books if book["level"] == level]

    if matched:
        return matched

    return books


st.title("📚 BookMatch")
st.subheader("관심사 기반 맞춤 도서 추천기")

st.write(
    "관심 분야와 독서 취향을 입력하면 어울리는 도서를 추천합니다."
)

category = st.selectbox(
    "관심 분야",
    ["", *BOOK_DB.keys()]
)

taste = st.text_input(
    "취향 입력 (예: 실무 위주, 재미있는 책, 깊이 있는 내용)"
)

purpose = st.selectbox(
    "독서 목적",
    ["", "공부", "취미", "자기계발", "업무 활용"]
)

level = st.radio(
    "선호 난이도",
    ["입문", "중급", "고급"]
)

col1, col2 = st.columns(2)

with col1:
    recommend_btn = st.button("📖 추천받기")

with col2:
    random_btn = st.button("🎲 랜덤 추천")

if recommend_btn:
    if not category:
        st.warning("관심 분야를 선택해주세요.")
    else:
        results = recommend_books(category, level)

        if results:
            st.success("추천 결과")

            for book in results:
                st.markdown(f"### 📘 {book['title']}")
                st.write(f"**난이도:** {book['level']}")
                st.write(f"**추천 이유:** {book['reason']}")

                if taste:
                    st.write(
                        f"입력한 취향('{taste}')과 연관하여 참고해볼 만한 도서입니다."
                    )

                if purpose:
                    st.write(f"독서 목적: {purpose}")

                st.divider()
        else:
            st.info("조건에 맞는 도서를 찾지 못했습니다.")

if random_btn:
    category = random.choice(list(BOOK_DB.keys()))
    book = random.choice(BOOK_DB[category])

    st.success("오늘의 랜덤 추천")

    st.markdown(f"### 📚 {book['title']}")
    st.write(f"분야: {category}")
    st.write(f"난이도: {book['level']}")
    st.write(f"추천 이유: {book['reason']}")

st.markdown("---")
st.caption("Made with Streamlit")
