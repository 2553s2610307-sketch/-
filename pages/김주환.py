import streamlit as st
import random
import time

st.set_page_config(
    page_title="📚 책 추천 룰렛",
    page_icon="📚",
    layout="centered"
)

st.title("📚 오늘 읽을 책 추천 룰렛")
st.write("읽고 싶은 장르를 선택하고 룰렛을 돌려보세요!")

# 장르별 책 데이터
books = {
    "소설": [
        "1984 - 조지 오웰",
        "데미안 - 헤르만 헤세",
        "연금술사 - 파울로 코엘료",
        "죄와 벌 - 도스토옙스키",
        "채식주의자 - 한강"
    ],
    "판타지": [
        "해리 포터와 마법사의 돌 - J.K. 롤링",
        "반지의 제왕 - J.R.R. 톨킨",
        "어스시의 마법사 - 어슐러 르 귄",
        "나니아 연대기 - C.S. 루이스",
        "위쳐 - 안제이 사프콥스키"
    ],
    "추리": [
        "그리고 아무도 없었다 - 애거서 크리스티",
        "셜록 홈즈 - 아서 코난 도일",
        "Y의 비극 - 엘러리 퀸",
        "용의자 X의 헌신 - 히가시노 게이고",
        "백야행 - 히가시노 게이고"
    ],
    "자기계발": [
        "아주 작은 습관의 힘",
        "원씽",
        "성공하는 사람들의 7가지 습관",
        "그릿",
        "딥 워크"
    ],
    "과학": [
        "코스모스 - 칼 세이건",
        "이기적 유전자 - 리처드 도킨스",
        "시간의 역사 - 스티븐 호킹",
        "사피엔스 - 유발 하라리",
        "떨림과 울림 - 김상욱"
    ]
}

genre = st.selectbox(
    "장르를 선택하세요",
    list(books.keys())
)

if st.button("🎲 룰렛 돌리기"):
    roulette = st.empty()

    candidates = books[genre]

    # 룰렛 애니메이션
    for _ in range(20):
        roulette.markdown(
            f"## 🎯 {random.choice(candidates)}"
        )
        time.sleep(0.1)

    selected_book = random.choice(candidates)

    roulette.markdown(
        f"""
        ## 📖 추천 도서

        ### {selected_book}
        """
    )

    st.balloons()

st.divider()

st.caption("오늘의 독서 운을 시험해보세요 📚✨")
