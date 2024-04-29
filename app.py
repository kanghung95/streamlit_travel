import streamlit as st
from home import journey_home
from mobile import journey_mobile

def main() :
    st.title('국내여행 검색 1순위')
    st.subheader('모바일과 PC에서 뽑은 날짜별 국내여행지 1순위를 예측합니다')

    menu = ['Home', 'Mobile', 'PC', 'Total']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        journey_home()
    elif choice == menu[1] :
        journey_mobile()
    elif choice == menu[2] :
        pass

if __name__ == '__main__' :
    main()
