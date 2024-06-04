import utils.folium_graph as graph
from streamlit_folium import folium_static

folium_static(graph.get_graph('driving_distance', True))