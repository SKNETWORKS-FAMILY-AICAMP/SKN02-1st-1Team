import folium
import utils.folium_graph as graph
from streamlit_folium import folium_static
from streamlit_option_menu import option_menu
from collections import Counter
import matplotlib.pyplot as plt
import json
import pandas as pd
import streamlit as st

### 변수 ###



### CLASS DECLARE ###
class View:
    def __init__(self, qna):
        self.qna = qna

    # def ViewFAQ(self, opt):
    #     with st.container():
    #         result = self.qna[self.qna['분류'] == opt]  

    #         for i in range(len(result)):            
    #             with st.expander(result['질문'][i]):
    #                 st.write(
    #                 result['답변'][i]
    #             )
    

    def ViewAllFAQ(self):
        with st.container():
            for i in range(len(self.qna['질문'])):
                with st.expander(self.qna['질문'][i]):
                    st.write(
                    self.qna['답변'][i]
                    )
                    
##########################

#####################################################33
# count_res = Counter(df['주소'])
df3 = pd.read_csv('./data/autooasis_store.csv')
count_res = Counter(df3['address_code'])

# 대한민국 시,군,구의 경계 GeoJSON 파일 경로
geojson_path = 'data/geo_sig.json' 

# 시,군,구 경계 GeoJSON 파일 로드
geo_data = json.load(open(geojson_path, encoding='utf-8'))

# 지점이 없는 시,군,구는 GeoJSON 파일에서 데이터 제거
for feature in geo_data['features']:
    region_name = feature['properties']['SIG_CD']
    if region_name not in count_res:
        geo_data['features'].remove(feature)

# Folium 지도 초기화

m = folium.Map(location=[36.5, 127.5], zoom_start=6)

folium.GeoJson(
    geo_data,
    name='지역구',
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 1,
        "dashArray": "5, 5",
    }
).add_to(m)

folium.Choropleth(geo_data=geo_data,
             data=count_res  , 
             fill_color='YlOrRd', # 색상 변경도 가능하다
             fill_opacity=0.7,
             line_opacity=0.2,
             key_on='properties.SIG_CD',
             legend_name="지역구별 Auto Oasis 지점 수",
            nan_fill_color="white",
            line_color='red',
            line_weight=0.3
            ).add_to(m)

########################################################
#####################################################33
# count_res = Counter(df['주소'])
df4 = pd.read_csv('./data/speedmate_store.csv')
count_res_2 = Counter(df4['address_code'])

# 지점이 없는 시,군,구는 GeoJSON 파일에서 데이터 제거
for feature in geo_data['features']:
    region_name = feature['properties']['SIG_CD']
    if region_name not in count_res:
        geo_data['features'].remove(feature)

# Folium 지도 초기화

m2 = folium.Map(location=[36.5, 127.5], zoom_start=6)

folium.GeoJson(
    geo_data,
    name='지역구',
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 1,
        "dashArray": "5, 5",
    }
).add_to(m2)

folium.Choropleth(geo_data=geo_data,
             data=count_res_2  , 
             fill_color='YlOrRd', # 색상 변경도 가능하다
             fill_opacity=0.7,
             line_opacity=0.2,
             key_on='properties.SIG_CD',
             legend_name="지역구별 Speedmate 지점 수",
            nan_fill_color="white",
            line_color='red',
            line_weight=0.3
            ).add_to(m2)

########################################################

### HEAD SETTING ###
head1, head2 = st.columns([3,1])

st.image('img/h1_speedMate01.png')
st.title('자동차 현황 및 영업점 분석')

# st.title('_Streamlit_ is :blue[cool] :sunglasses:')

### TAP SETTING ###
tab1, tab2, tab3, FAQ = st.tabs(['전국 자동차 등록 현황', '전국 자동차 통행량', '영업장', 'FAQ'])
f_faq = pd.read_csv('data/speedmate_faq.csv')
f_faq_c = pd.DataFrame(f_faq)
f_faq_c = f_faq_c.drop_duplicates(['분류'])


                    
Faq = View(f_faq)
data = pd.read_csv('./data/car_enrollment_year.csv', encoding='EUC-KR')
year_ls = list(range(2018,2024))
data2 = []

for year in year_ls :
    data2.append(data[str(year)][4])

chart_data = pd.DataFrame(data2, year_ls)

with tab1:
    st.header('전국 자동차 등록현황')
    fig = plt.figure()
    plt.bar(year_ls, data2)
    plt.ylim([22000000,27000000])
    st.pyplot(fig)

with tab2:
    st.header('전국 자동차 통행량')
    folium_static(graph.get_graph('driving_distance', True))

with tab3:
    st.header('영업장 비교')
    col1, col2 =  st.columns([1,1])
    with col1 :
        st.subheader('Speedmate 영업장')
        folium_static(m2, width=350, height=350)
    with col2 : 
        st.subheader('Auto Oasis 영업장')
        folium_static(m, width=350, height=350)

with FAQ:
    st.header('Speed Mate FAQ')
    
    Faq.ViewAllFAQ()

    st.divider()



