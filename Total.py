import streamlit as st
import pandas as pd
from datetime import datetime

def select_date_range():
    start_date = datetime(2024, 4, 1)
    end_date = datetime(2024, 4, 24)
    selected_date = st.date_input('날짜를 선택하세요', start_date, min_value=start_date, max_value=end_date, key='date_input')
    return selected_date

def journey_Total():
    st.subheader('날짜별 모바일 및 PC를 합친 검색순위를 알고싶다면?')
    
    df = pd.read_csv('travel/2024_travel.csv')
    df['검색 한 날짜'] = pd.to_datetime(df['검색 한 날짜'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    df.groupby('검색 한 날짜')

    selected_date = select_date_range()
    st.write('선택한 날짜:', selected_date)

    selectbox_menu_total_rank = ['모바일 및 PC 통합 순위', '모바일 통합 순위', 'PC 통합 순위']
    choice_sele_total_rank = st.selectbox('통합 순위를 선택하세요.', [''] + selectbox_menu_total_rank, key='total_rank_selection')

    
    if choice_sele_total_rank:
        target_date = selected_date.strftime('%Y-%m-%d')
        df_data = df[df['검색 한 날짜'] == target_date]
        if choice_sele_total_rank == '모바일 및 PC 통합 순위':
            df_data['통합 검색 횟수'] = df_data['모바일 검색 횟수'] + df_data['PC 검색 횟수']
            df_data = df_data.sort_values(by='통합 검색 횟수', ascending=False)
            st.dataframe(df_data)
            st.write(f'{selected_date} 모바일 및 PC 통합 순위 데이터입니다.')
        elif choice_sele_total_rank == '모바일 통합 순위':
            df_data = df_data.sort_values(by='모바일 검색 횟수', ascending=False)
            st.dataframe(df_data)
            st.write(f'{selected_date} 모바일 통합 순위 데이터입니다.')
        elif choice_sele_total_rank == 'PC 통합 순위':
            df_data = df_data.sort_values(by='PC 검색 횟수', ascending=False)
            st.dataframe(df_data)
            st.write(f'{selected_date} PC 통합 순위 데이터입니다.')

    st.subheader('날짜별 모바일 및 PC 검색 순위를 알고싶다면?')

    radio_menu = ['Mobile', 'PC']
    selected_device = st.radio('알고싶은 기기를 골라주세요!', radio_menu)

    selectbox_menu_individual_rank = ['1위', '2위', '3위']
    choice_sele_individual_rank = st.selectbox('개별 순위를 선택하세요.', [''] + selectbox_menu_individual_rank, key='individual_rank_selection')

    if choice_sele_individual_rank:
        target_date = selected_date.strftime('%Y-%m-%d')
        df_data = df[df['검색 한 날짜'] == target_date]
        if choice_sele_individual_rank == '1위':
            if selected_device == 'Mobile':
                df_max = df_data['모바일 검색 횟수'].max()
                st.dataframe(df_data[df_data['모바일 검색 횟수'] == df_max])
                st.write(f'{selected_date} 모바일에서 검색한 1위 여행지입니다!')
            elif selected_device == 'PC':
                df_max = df_data['PC 검색 횟수'].max()
                st.dataframe(df_data[df_data['PC 검색 횟수'] == df_max])
                st.write(f'{selected_date} PC에서 검색한 1위 여행지입니다!')
        elif choice_sele_individual_rank == '2위':
            if selected_device == 'Mobile':
                df_max = df_data['모바일 검색 횟수'].nlargest(2).iloc[-1]
                st.dataframe(df_data[df_data['모바일 검색 횟수'] == df_max])
                st.write(f'{selected_date} 모바일에서 검색한 2위 여행지입니다!')
            elif selected_device == 'PC':
                df_max = df_data['PC 검색 횟수'].nlargest(2).iloc[-1]
                st.dataframe(df_data[df_data['PC 검색 횟수'] == df_max])
                st.write(f'{selected_date} PC 2위에서 검색한 여행지입니다!')
        elif choice_sele_individual_rank == '3위':
            if selected_device == 'Mobile':
                df_max = df_data['모바일 검색 횟수'].nlargest(3).iloc[-1]
                st.dataframe(df_data[df_data['모바일 검색 횟수'] == df_max])
                st.write(f'{selected_date} 모바일에서 검색한 3위 여행지입니다!')
            elif selected_device == 'PC':
                df_max = df_data['PC 검색 횟수'].nlargest(3).iloc[-1]
                st.dataframe(df_data[df_data['PC 검색 횟수'] == df_max])
                st.write(f'{selected_date} PC에서 검색한 3위 여행지입니다!')

journey_Total()