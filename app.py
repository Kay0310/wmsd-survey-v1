
import streamlit as st

st.set_page_config(page_title="근골격계 증상조사", layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo/WMSD.png", width=150)

st.title("근골격계 증상조사")
st.markdown("---")
st.success("앱이 정상 작동 중입니다.\n\n✍️ 설문 시스템은 다음 단계에서 연결됩니다.")
