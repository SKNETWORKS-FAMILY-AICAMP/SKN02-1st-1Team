import folium
from streamlit_folium import folium_static
from collections import Counter
import json
import pandas as pd
from .db_connector import Connector

def get_graph(table_name, total=False) :
    SQL = f'SELECT * FROM {table_name}'
    print(SQL)
    # db 커넥션을 이용해 데이터를 pandas dataframe으로 변환함
    conn = Connector.get_connection()
    df3 = pd.read_sql(SQL, conn)
    conn.close()
    result = None

    if total :
        result = dict(zip(df3['addr_code'], df3['total']))
    else :
        result = Counter(df3['addr_code'])

    # 대한민국 시,군,구의 경계 GeoJSON 파일 경로
    geojson_path = 'data/geo_sig.json' 

    # 시,군,구 경계 GeoJSON 파일 로드
    geo_data = json.load(open(geojson_path, encoding='utf-8'))


    # Folium 지도 초기화
    m = folium.Map(location=[36.5, 127.5], zoom_start=7)

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
                data=result, 
                fill_color='YlOrRd', # 색상 변경도 가능하다
                fill_opacity=0.7,
                line_opacity=0.2,
                key_on='properties.SIG_CD',
                legend_name="지역구별 autooasis 지점 수",
                nan_fill_color="white",
                line_color='red',
                line_weight=0.3
                ).add_to(m)

    return m
