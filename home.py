import streamlit as st

def journey_home() :
    st.subheader('모바일과 PC에서 검색한 인기 여행지역은 어디일까요?')
    st.text('국내여행 데이터는 문화 빅데이터 플랫폼에서 도움을 받았으며')
    st.text('2024년 4월1일부터 24일까지의 데이터를 다운받아 합친')
    st.text('2024_travel.csv 파일을 사용하였습니다.')

    st.subheader('플랫폼 들어가기')
    st.write('https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=25c89d50-1e55-11eb-a4e6-a9a03a61580b')
    st.image('./way.jpg', use_column_width=True)
