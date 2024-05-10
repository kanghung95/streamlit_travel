import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime, timedelta

def select_date_range():
    start_date = datetime(2024, 5, 1)
    end_date = datetime(2024, 12, 31)
    selected_date = st.date_input('날짜를 선택하세요', start_date, min_value=start_date, max_value=end_date, key='date_input')
    return selected_date

def journey_ml():
    st.subheader('5월부터의 추천지역 확인해보기')
    st.text('날짜와 여행지를 선택하면 지역을 추천해드려요!')

    selected_date = select_date_range() 

    cities = ['부산', '경주', '제주', '여수', '군산', '강릉', '전주', '속초', '목포', '대구', '대전', '남해']
    city = st.selectbox('여행지 선택', cities)

    encoded_city = [0] * len(cities)
    encoded_city[cities.index(city)] = 1

    st.subheader('이날의 인기지역은?')

    if st.button('지역추천 받아보기'):
        df = pd.read_csv('travel/2024_travel.csv')
        df['검색 한 날짜'] = pd.to_datetime(df['검색 한 날짜'], format='%Y%m%d').dt.strftime('%Y-%m-%d')

        travel = joblib.load('./model/regressor_travel.pkl')
        
        new_data = np.array(encoded_city[:5]).reshape(1, -1)
        city_travel = travel.predict(new_data)
        
        recommended_city_index = np.argmax(city_travel)
        recommended_city = cities[recommended_city_index]

        selected_date_str = selected_date.strftime('%Y-%m-%d')
        st.text(f"{selected_date_str} 예상으로는 {city}보다는 {recommended_city}을(를) 추천드립니다!")
    
        if recommended_city == city :
            st.write(f"저도 {city}를 추천합니다!")
        
        if recommended_city == '부산':
            st.image('./image/부산.jpg', caption='부산의 아름다운 풍경', use_column_width=True)
            st.write("부산은 해변과 맛집이 유명합니다. 여행자들에게 인기 있는 명소로는 해운대 해수욕장과 광안리 해수욕장이 있습니다.")
        elif recommended_city == '경주':
            st.image('./image/rudwn.jpg', caption='경주의 유적지', use_column_width=True)
            st.write("경주는 한국의 역사와 문화를 엿볼 수 있는 곳입니다. 세계문화유산으로 등재된 불국사와 석굴암은 꼭 방문해볼 만한 곳입니다.")
        elif recommended_city == '제주':
            st.image('./image/제주.jpg', caption='제주의 자연경관', use_column_width=True)
            st.write("제주는 자연 경관이 아름답고 여행 명소가 풍부합니다. 용눈이오름, 성산일출봉, 한라산 등이 대표적인 관광지입니다.")
        elif recommended_city == '여수':
            st.image('./image/여수.jpg', caption='여수의 야경', use_column_width=True)
            st.write("여수는 바다와 도시의 만남으로 유명합니다. 여수밤바다를 대표하는 여수 해상케이블카와 여수 엑스포해마루를 추천합니다.")
        elif recommended_city == '군산':
            st.image('./image/군산.jpg', caption='군산의 전통 마을', use_column_width=True)
            st.write("군산은 전통적인 한옥 마을과 독특한 문화를 느낄 수 있는 곳입니다. 옥도면 외항항 등이 관광지로 유명합니다.")
        elif recommended_city == '강릉':
            st.image('./image/강릉.jpg', caption='강릉의 바다', use_column_width=True)
            st.write("강릉은 동해바다를 바라보며 여유를 즐길 수 있는 곳입니다. 강릉은 바다와 산이 어우러진 아름다운 자연 경관이 특징입니다.")
        elif recommended_city == '전주':
            st.image('./image/전주.jpg', caption='전주의 한옥마을', use_column_width=True)
            st.write("전주는 한국의 전통 문화와 음식을 경험할 수 있는 곳입니다. 전주한옥마을과 한옥마을 내 맛집들을 추천합니다.")
        elif recommended_city == '속초':
            st.image('./image/속초.jpg', caption='속초의 동북아 해변', use_column_width=True)
            st.write("속초는 동북아 해변을 감싸고 있는 아름다운 도시입니다. 남이섬과 속초해변 등이 인기 있는 관광지입니다.")
        elif recommended_city == '목포':
            st.image('./image/목포.jpg', caption='목포의 바다와 섬', use_column_width=True)
            st.write("목포는 바다와 섬이 어우러진 아름다운 도시입니다. 여러 해상 관광지와 맛집이 있는데, 목포대교와 연꽃으로 유명합니다.")
        elif recommended_city == '대구':
            st.image('./image/대구.jpg', caption='대구의 도심', use_column_width=True)
            st.write("대구는 도심과 자연이 조화를 이루는 도시입니다. 앞산공원과 이월드 등이 대표적인 관광지입니다.")
        elif recommended_city == '대전':
            st.image('./image/대전.jpg', caption='대전의 센터시티', use_column_width=True)
            st.write("대전은 교통 요지로 위치하여 다양한 관광 명소가 있습니다. 대청호와 오월드가 대표적인 관광지입니다.")
        elif recommended_city == '남해':
            st.image('./image/남해.jpg', caption='남해의 풍경', use_column_width=True)
            st.write("남해는 아름다운 해안선과 자연 풍경을 자랑하는 곳입니다. 남해돔과 섬진강 등이 인기 있는 관광지입니다.")

if __name__ == '__main__':
    journey_ml()