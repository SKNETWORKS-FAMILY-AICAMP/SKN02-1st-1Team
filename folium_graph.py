import folium
from streamlit_folium import folium_static
from collections import Counter
import json
import pandas as pd
#지역별 count


# count_res = Counter(df['주소'])
df3 = pd.read_csv('./data/autooasis_store.csv')
count_res = Counter(df3['address_code'])

# 대한민국 시,군,구의 경계 GeoJSON 파일 경로
geojson_path = 'TL_SCCO_SIG.json' 

# 시,군,구 경계 GeoJSON 파일 로드
geo_data = json.load(open(geojson_path, encoding='utf-8'))

# 지점이 없는 시,군,구는 GeoJSON 파일에서 데이터 제거
for feature in geo_data['features']:
    region_name = feature['properties']['SIG_CD']
    if region_name not in count_res:
        geo_data['features'].remove(feature)
# Folium 지도 초기화

m = folium.Map(location=[36.5, 127.5], zoom_start=7)

folium.GeoJson(
    geo_data,
    name='지역구'
).add_to(m)

folium.Choropleth(geo_data=geo_data,
             data=count_res  , 
             fill_color='YlOrRd', # 색상 변경도 가능하다
             fill_opacity=0.7,
             line_opacity=0.2,
             key_on='properties.SIG_CD',
             legend_name="지역구별 autooasis 지점 수"
            ).add_to(m)

# # Counter 데이터 반복하며 Folium 지도에 마커 표시
# for region, count in counter_data.items():
#     # 해당 지역의 경계 GeoJSON 가져오기
#     feature = next((feat for feat in geo_data['features'] if feat['properties']['SIG_KOR_NM'] == region), None)
#     if feature:
#         # 지역 경계를 기반으로 Polygon 생성
#         folium.GeoJson(feature,
#                        style_function=lambda x: {'fillColor': 'red', 'fillOpacity': 0.5}).add_to(m)

# Folium 지도를 Streamlit에 표시
folium_static(m)