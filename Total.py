import streamlit as st
import pandas as pd
import joblib
from datetime import datetime, timedelta

def select_date_range():
    start_date = datetime(2024, 4, 1)
    end_date = datetime(2024, 4, 24)
    selected_date = st.date_input('날짜를 선택하세요', start_date, min_value=start_date, max_value=end_date, key='date_input')
    return selected_date

def journey_Total():
    st.subheader('날짜별 모바일 및 PC 검색 순위와 합친 순위 데이터를 보여드립니다.')
    
    df = pd.read_csv('travel/2024_travel.csv')
    df['검색 한 날짜'] = pd.to_datetime(df['검색 한 날짜'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    df.groupby('검색 한 날짜')
    st.dataframe(df)

    # 날짜를 먼저 선택
    selected_date = select_date_range()
    st.write('선택한 날짜:', selected_date)

    # 모바일 횟수와 PC 횟수를 합친 순위를 보여줄 수 있도록 변경
    selectbox_menu = ['모바일 및 PC 통합 순위', '모바일 통합 순위', 'PC 통합 순위']
    choice_sele = st.selectbox('순위를 선택하세요.', selectbox_menu, key='rank_selection')

    # 순위 선택에 따라 처리
    if choice_sele == '모바일 및 PC 통합 순위':
        target_date = selected_date.strftime('%Y-%m-%d')
        df_data = df[df['검색 한 날짜'] == target_date]
        df_data['통합 검색 횟수'] = df_data['모바일 검색 횟수'] + df_data['PC 검색 횟수']
        df_data = df_data.sort_values(by='통합 검색 횟수', ascending=False)
        st.dataframe(df_data)
        st.write('모바일 및 PC 통합 순위 데이터입니다.')
        
    elif choice_sele == '모바일 통합 순위':
        target_date = selected_date.strftime('%Y-%m-%d')
        df_data = df[df['검색 한 날짜'] == target_date]
        df_data = df_data.sort_values(by='모바일 검색 횟수', ascending=False)
        st.dataframe(df_data)
        st.write('모바일 통합 순위 데이터입니다.')
        
    elif choice_sele == 'PC 통합 순위':
        target_date = selected_date.strftime('%Y-%m-%d')
        df_data = df[df['검색 한 날짜'] == target_date]
        df_data = df_data.sort_values(by='PC 검색 횟수', ascending=False)
        st.dataframe(df_data)
        st.write('PC 통합 순위 데이터입니다.')

journey_Total()