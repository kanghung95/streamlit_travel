import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime

def select_date_range():
    start_date = datetime(2024, 4, 1)
    end_date = datetime(2024, 4, 24)
    selected_date = st.date_input('날짜를 선택하세요', start_date, min_value=start_date, max_value=end_date, key='date_input')
    return selected_date

def journey_ml():
    st.subheader('여행 예측')
    st.text('날짜와 여행지를 선택하면 해당 인기지역을 소개시켜드립니다!')

    selected_date = select_date_range()  # 먼저 날짜를 선택하도록 변경

    cities = ['부산', '경주', '제주', '여수', '군산', '강릉', '전주', '속초', '목포', '대구', '대전', '남해']
    city = st.selectbox('여행지 선택', cities)

    encoded_city = [0] * len(cities)
    encoded_city[cities.index(city)] = 1

    st.subheader('이날의 인기지역은?')

    if st.button('지역보기'):
        df = pd.read_csv('travel/2024_travel.csv')
        df['검색 한 날짜'] = pd.to_datetime(df['검색 한 날짜'], format='%Y%m%d').dt.strftime('%Y-%m-%d')

        travel = joblib.load('./model/regressor_travel.pkl')
        new_data = np.array([encoded_city + []]).reshape(1, -1)
        city_travel = travel.predict(new_data)
        st.text(f'제일 많이 검색한 지역은 {city_travel} 입니다!')

if __name__ == '__main__':
    journey_ml()