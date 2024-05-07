import streamlit as st
from home import journey_home
from Total import journey_Total
from ml import journey_ml

import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def main() :
    st.title('날짜별 국내여행 순위를 알아보자')

    menu = ['Home', 'Total', 'ML']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        journey_home()
    elif choice == menu[1] :
        journey_Total()
    elif choice == menu[2] :
        journey_ml()
        

if __name__ == '__main__' :
    main()
