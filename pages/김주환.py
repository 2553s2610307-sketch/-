import streamlit as st

st.set_page_config(page_title="진로 도서 추천", page_icon="🎯")

# 📚 진로별 도서 데이터
BOOKS = [
    {
        "career": "의사",
        "field": "과학",
        "title": "숨결이 바람 될 때",
        "level": "어려움",
        "desc": "의사의 삶과 죽음에 대한 철학적 성찰",
        "skill": "공감력, 책임감"
    },
    {
        "career": "의사",
        "field": "과학",
        "title": "아내를 모자로 착각한 남자",
        "level": "보통",
        "desc": "뇌와 인간 행동에 대한 실제 사례",
        "skill": "관찰력"
    },
    {
        "career": "개발자",
        "field": "기술",
        "title": "코딩을 지탱하는 기술",
        "level": "보통",
        "desc": "프로그래밍 사고 방식 이해",
        "skill": "논리력"
    },
    {
        "career": "개발자",
        "field": "기술",
        "title": "클린 코드",
        "level": "어려움",
        "desc": "좋은 코드 작성 방법",
        "skill": "문제 해결력"
    },
    {
        "career": "교사",
        "field": "인문",
        "title": "배움의 발견",
        "level": "보통",
        "desc": "교육과 성장의 의미",
        "skill": "소통 능력"
    },
    {
        "career": "경찰",
        "field": "사회",
        "title": "프로파일링",
        "level": "보통",
        "desc": "범죄 심리 분석",
        "skill": "분석력"
    },
    {
        "career": "디자이너",
        "field": "예술",
        "title": "디자인의 디자인",
        "level": "쉬움",
        "desc": "디자인 사고의 본질",
        "skill": "창의력"
    },
    {
        "career": "유튜버",
        "field": "사회",
        "title": "스토리텔링의 힘",
        "level": "쉬움",
        "desc": "콘텐츠 제작과 이야기 구성",
        "skill": "표현력"
    },
    {
        "career": "연구원",
        "field": "과학",
        "title": "이기적 유전자",
        "level": "어려움",
        "desc": "진화생물학 핵심 이론",
        "skill": "분석력"
    },
    {
        "career": "경영",
        "field": "사회",
        "title": "좋은 기업을 넘어 위대한 기업으로",
        "level": "보통",
        "desc": "경영 전략과 리더십",
        "skill": "전략적 사고"
    },
]


st.title("🎯 진로 맞춤 도서 추천")
st.write("희망 진로를 선택하면 관련 책을 추천해드립니다.")

try:
    # 🎛️ 사용자 입력
    career = st.selectbox(
        "희망 진로 선택",
        ["전체"] + sorted(list(set([b["career"] for b in BOOKS])))
    )

    field = st.selectbox(
        "관심 분야",
        ["전체", "인문", "과학", "기술", "사회", "예술"]
    )

    level = st.selectbox(
        "난이도",
        ["전체", "쉬움", "보통", "어려움"]
    )

    keyword = st.text_input("🔍 키워드 검색 (책 제목)", "")

    if st.button("📚 추천 받기"):
        results = BOOKS

        # 필터 적용
        if career != "전체":
            results = [b for b in results if b["career"] == career]

        if field != "전체":
            results = [b for b in results if b["field"] == field]

        if level != "전체":
            results = [b for b in results if b["level"] == level]

        if keyword:
            results = [b for b in results if keyword.lower() in b["title"].lower()]

        # 결과 출력
        st.subheader("📖 추천 결과")

        if results:
            for b in results:
                st.markdown(f"### 📘 {b['title']}")
                st.write(f"🎯 진로: {b['career']}")
                st.write(f"📚 분야: {b['field']}")
                st.write(f"📊 난이도: {b['level']}")
                st.write(f"💡 추천 이유: {b['desc']}")
                st.write(f"🧠 키워드 역량: {b['skill']}")
                st.divider()
        else:
            st.warning("조건에 맞는 책이 없습니다. 필터를 변경해보세요.")

except Exception as e:
    st.error("앱 실행 중 오류가 발생했습니다.")
    st.write(e)
