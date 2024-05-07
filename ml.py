import streamlit as st
import joblib
import numpy as np

def journey_ml() :
    st.subheader('여행 예측')


    st.text('검색도구를 선택하세요')
    search = st.radio('검색도구 선택', ['Mobile', 'PC'])
    if search == 'Mobile' :
        search = 1
    elif search == 'PC' :
        search = 0

    st.text('여행지역을 입력하세요')
    city = st.text_input('여행지역 입력', placeholder='부산, 경주, 제주, 여수, 군산, 강릉, 전주, 속초, 목포, 대구, 대전, 남해')

    st.text('Mobile 검색횟수를 입력하세요')
    mobile = st.number_input('Mobile 검색횟수 입력', min_value=100, max_value=2000, value=500, step=10)

    st.text('PC 검색횟수를 입력하세요')
    pc = st.number_input('PC 검색횟수 입력', min_value=10, max_value=1000, value=100, step=10)

    st.subheader('예측을 시작합니다.')

    if st.button('예측하기') :

        travel = joblib.load('./model/travel_model.pkl')
        print(travel)

        new_data = [city, mobile, pc]
        print(new_data)

        new_data = np.array(new_data).reshape(1, -1)

        city_travel = travel.predict(new_data)

        st.text(f'예측한 위치는 {city_travel}여행 입니다.')

