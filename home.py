import streamlit as st

def journey_home() :
    st.subheader('국내여행 검색 데이터를 분석하여 예측합니다.')
    st.text('국내여행 데이터는 문화 빅데이터 플랫폼에서 도움을 받았으며')
    st.text('2024.travel.csv 파일을 사용하였습니다.')

    st.image('./way.jpg', use_column_width=True)