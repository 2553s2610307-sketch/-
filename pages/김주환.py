import streamlit as st
import random

st.set_page_config(
    page_title="📚 Book Compass",
    page_icon="📚",
    layout="centered"
)

# -----------------------
# 책 데이터
# -----------------------

BOOKS = [
    {
        "title": "사피엔스",
        "author": "유발 하라리",
        "category": "인문",
        "mood": "생각이 많을 때",
        "goal": "지식 쌓기",
        "reason": "인류의 역사를 넓은 시각으로 바라볼 수 있습니다."
    },
    {
        "title": "아주 작은 습관의 힘",
        "author": "제임스 클리어",
        "category": "자기계발",
        "mood": "동기부여가 필요할 때",
        "goal": "성장",
        "reason": "작은 행동이 큰 변화를 만든다는 점을 알려줍니다."
    },
    {
        "title": "코스모스",
        "author": "칼 세이건",
        "category": "과학",
        "mood": "생각이 많을 때",
        "goal": "지식 쌓기",
        "reason": "우주와 과학을 쉽고 흥미롭게 설명합니다."
    },
    {
        "title": "데미안",
        "author": "헤르만 헤세",
        "category": "소설",
        "mood": "감성적인 날",
        "goal": "힐링",
        "reason": "자아를 찾아가는 여정을 담고 있습니다."
    },
    {
        "title": "1984",
        "author": "조지 오웰",
        "category": "소설",
        "mood": "생각이 많을 때",
        "goal": "지식 쌓기",
        "reason": "사회와 권력에 대해 깊게 생각하게 만듭니다."
    },
    {
        "title": "그릿",
        "author": "앤절라 더크워스",
        "category": "자기계발",
        "mood": "동기부여가 필요할 때",
        "goal": "성장",
        "reason": "성공의 핵심은 끈기라는 점을 알려줍니다."
    },
    {
        "title": "불편한 편의점",
        "author": "김호연",
        "category": "소설",
        "mood": "편안하게 읽고 싶을 때",
        "goal": "힐링",
        "reason": "따뜻한 이야기로 마음을 편안하게 해줍니다."
    },
    {
        "title": "떨림과 울림",
        "author": "김상욱",
        "category": "과학",
        "mood": "생각이 많을 때",
        "goal": "지식 쌓기",
        "reason": "과학을 인문학적 관점과 함께 설명합니다."
    }
]

# -----------------------
# 제목
# -----------------------

st.title("📚 Book Compass")
st.subheader("오늘의 독서 방향을 찾아보세요")

st.write(
    """
    관심 분야와 현재 상태를 선택하면
    어울리는 책을 추천해드립니다.
    """
)

# -----------------------
# 입력
# -----------------------

category = st.selectbox(
    "관심 분야",
    ["소설", "과학", "인문", "자기계발"]
)

mood = st.selectbox(
    "현재 기분",
    [
        "생각이 많을 때",
        "감성적인 날",
        "동기부여가 필요할 때",
        "편안하게 읽고 싶을 때"
    ]
)

goal = st.selectbox(
    "독서 목적",
    [
        "힐링",
        "성장",
        "지식 쌓기"
    ]
)

# -----------------------
# 추천
# -----------------------

if st.button("📖 책 추천받기"):

    try:
        matches = [
            book for book in BOOKS
            if (
                book["category"] == category
                or book["mood"] == mood
                or book["goal"] == goal
            )
        ]

        if not matches:
            matches = BOOKS

        recommendation = random.choice(matches)

        st.success("추천 도서가 선정되었습니다!")

        st.markdown("---")

        st.markdown(
            f"""
### 📚 {recommendation['title']}

**저자**  
{recommendation['author']}

**추천 이유**  
{recommendation['reason']}
"""
        )

        st.info(
            f"""
관심 분야: {recommendation['category']}

독서 목적: {recommendation['goal']}
"""
        )

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

# -----------------------
# 하단
# -----------------------

st.markdown("---")
st.caption("오늘의 독서가 더 즐거워지길 바랍니다 📖")
