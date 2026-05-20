
import streamlit as st
import json
import os

FILE_NAME = "schedule.json"

# 파일 없으면 생성
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([], f)

# 데이터 불러오기
with open(FILE_NAME, "r", encoding="utf-8") as f:
    schedules = json.load(f)

st.title("📅 스케줄 관리")

# 일정 입력
new_schedule = st.text_input("새 일정 입력")

# 추가 버튼
if st.button("추가"):
    if new_schedule.strip() != "":
        schedules.append({
            "task": new_schedule,
            "done": False
        })

        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(schedules, f, ensure_ascii=False)

        st.success("일정 추가 완료")
        st.rerun()

# 일정 표시
st.subheader("일정 목록")

for i, item in enumerate(schedules):
    checked = st.checkbox(
        item["task"],
        value=item["done"],
        key=i
    )

    schedules[i]["done"] = checked

# 저장
with open(FILE_NAME, "w", encoding="utf-8") as f:
    json.dump(schedules, f, ensure_ascii=False)

# 완료 개수
done_count = sum(item["done"] for item in schedules)

st.write(f"완료: {done_count} / {len(schedules)}")
