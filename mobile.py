import streamlit as st
import pandas as pd


def journey_mobile() :
    st.subheader('날짜별 모바일에서의 순위를 알아보자.')

    df = pd.read_csv('travel/2024_travel.csv')
    df.drop(['Sequence Number', 'Top 10 rankings by date'], axis=1)

    st.dataframe(df)