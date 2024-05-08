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

    menu = ['메인화면', '통합 및 개별순위', '인기여행지']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        journey_home()
    elif choice == menu[1] :
        journey_Total()
    elif choice == menu[2] :
        journey_ml()
        

if __name__ == '__main__' :
    main()
