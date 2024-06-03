import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
from streamlit_option_menu import option_menu

st.title('자동차 현황 및 스피드메이트 영업점 분석')
# st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# 대한민국 전국 지도
# m = folium.Map(location=[38.0, 127], zoom_start=6)

# # 지도 위에 마커 달기
# folium.Marker(
#     [37.0, 127.25],
#     popup="Hello",
#     tooltip="tooltip"

# ).add_to(m)

# st_data = st_folium(m, width = 725)

# col1, col2 = st.columns([2,3])

# with col1 :
#     st.title('column 1')
# with col2 :
#     st.title('column2')
#     st.checkbox('this is check box')

tab1, tab2, tab3, FAQ = st.tabs(['전국 자동차 등록 현황', '전국 자동차 통행량', '영업장', 'FAQ'])
f_faq = pd.read_csv('./result.csv')


with tab1:
    st.header('전국 자동차 등록현황')
with tab2:
    st.header('전국 자동차 통행량')
with tab3:
    st.header('영업장')
with FAQ:
    st.header('FAQ')
    # # 2. horizontal menu
    # selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    # menu_icon="cast", default_index=0, orientation="horizontal")
    # selected2
    
    for i in range(len(f_faq['분류'])):
        with st.expander(f_faq['분류'][i]):
            st.write(
                f_faq['답변'][i]
            )
    # st.write(f_faq)

# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Side1", 'Side2'], 
#         icons=['smile', 'house'], menu_icon="cast", default_index=1)
#     selected

