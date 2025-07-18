import streamlit as st

# ✅ 브라우저 탭 제목 및 레이아웃 설정 (모바일 대응)
st.set_page_config(
    page_title="GOIT 버킷리스트 매칭 플랫폼",
    page_icon="🌈",
    layout="centered",  # 'wide'로 하면 모바일에서 깨질 수 있음
    initial_sidebar_state="collapsed"  # 모바일에서는 사이드바 자동 숨김
)

# ✅ 제목
st.markdown("<h1 style='text-align: center;'>🌟 GOIT 버킷리스트 매칭</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>당신의 꿈과 현실을 함께 엮어보세요.</p>", unsafe_allow_html=True)

# ✅ 입력창 UI
bucket = st.text_input("🌈 당신의 꿈은 무엇인가요?", placeholder="예: 유튜브 출연하기")
reality = st.text_input("✨ 당신이 가진 현실은?", placeholder="예: 유튜버입니다")

# ✅ 등록 버튼
if st.button("등록하기"):
    if bucket and reality:
        with open("bucket_list.txt", "a", encoding="utf-8") as f:
            f.write(f"꿈: {bucket} / 현실: {reality}\n")
        st.success("저장되었습니다!")
    else:
        st.warning("모든 항목을 입력해주세요.")

# ✅ 리스트 보기
st.subheader("📋 등록된 매칭 리스트")

try:
    with open("bucket_list.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            st.markdown(f"<div style='padding: 8px; border-bottom: 1px solid #eee; font-size: 16px;'>👉 {line.strip()}</div>", unsafe_allow_html=True)
except FileNotFoundError:
    st.info("아직 등록된 데이터가 없습니다.")
