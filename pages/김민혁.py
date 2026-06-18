import streamlit as st

st.set_page_config(page_title="수행평가 도서 추천", page_icon="📘")

# 📚 도서 데이터 (간단하고 안정적인 구조)
BOOKS = [
    {
        "title": "1984",
        "subject": "인문",
        "level": "고등",
        "type": "토론",
        "length": "중",
        "desc": "전체주의 사회를 비판하는 디스토피아 소설"
    },
    {
        "title": "멋진 신세계",
        "subject": "인문",
        "level": "고등",
        "type": "토론",
        "length": "중",
        "desc": "통제된 미래 사회를 그린 작품"
    },
    {
        "title": "아몬드",
        "subject": "국어",
        "level": "중등",
        "type": "독서감상문",
        "length": "중",
        "desc": "감정을 느끼지 못하는 소년의 성장 이야기"
    },
    {
        "title": "죽은 시인의 사회",
        "subject": "국어",
        "level": "고등",
        "type": "독서감상문",
        "length": "중",
        "desc": "자유로운 교육과 삶의 의미"
    },
    {
        "title": "과학 콘서트",
        "subject": "과학",
        "level": "중등",
        "type": "보고서",
        "length": "짧음",
        "desc": "일상 속 과학 원리를 쉽게 설명"
    },
    {
        "title": "총, 균, 쇠",
        "subject": "사회",
        "level": "고등",
        "type": "보고서",
        "length": "김",
        "desc": "문명 발전의 역사적 요인 분석"
    },
    {
        "title": "팩트풀니스",
        "subject": "사회",
        "level": "고등",
        "type": "보고서",
        "length": "중",
        "desc": "세상을 바라보는 데이터 기반 사고"
    },
    {
        "title": "청소년을 위한 진로 인문학",
        "subject": "진로",
        "level": "중등",
        "type": "보고서",
        "length": "짧음",
        "desc": "진로 탐색을 위한 기초 인문학"
    },
]


st.title("📘 수행평가 도서 추천 도우미")
st.write("조건을 선택하면 수행평가에 맞는 책을 추천해드립니다.")

try:
    # 🎛️ 사용자 입력
    level = st.selectbox("학년 선택", ["전체", "중등", "고등"])
    subject = st.selectbox("과목 선택", ["전체", "국어", "사회", "과학", "역사", "진로", "인문"])
    task_type = st.selectbox("수행평가 유형", ["전체", "보고서", "독서감상문", "토론"])
    length = st.selectbox("책 길이", ["전체", "짧음", "중", "김"])

    keyword = st.text_input("🔍 키워드 검색 (선택)", "")

    if st.button("📚 추천받기"):
        results = BOOKS

        # 필터 적용
        if level != "전체":
            results = [b for b in results if b["level"] == level]

        if subject != "전체":
            results = [b for b in results if b["subject"] == subject]

        if task_type != "전체":
            results = [b for b in results if b["type"] == task_type]

        if length != "전체":
            results = [b for b in results if b["length"] == length]

        if keyword:
            results = [b for b in results if keyword.lower() in b["title"].lower()]

        # 결과 출력
        st.subheader("📖 추천 결과")

        if results:
            for b in results:
                st.markdown(f"### 📕 {b['title']}")
                st.write(f"- 과목: {b['subject']}")
                st.write(f"- 추천 유형: {b['type']}")
                st.write(f"- 난이도/길이: {b['length']}")
                st.write(f"- 설명: {b['desc']}")
                st.divider()
        else:
            st.warning("조건에 맞는 책이 없습니다. 조건을 변경해보세요.")

except Exception as e:
    st.error("오류가 발생했습니다. 입력 조건을 확인해주세요.")
    st.write(e)
