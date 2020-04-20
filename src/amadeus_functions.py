import folium

def add_points_to_map(mapa,df,category,dict_colors):
    for latitude,longitude,category in df[["latitude","longitude",category]].values:
        folium.Circle(
        radius=100,
        location=[latitude,longitude],
        color=dict_colors[category],).add_to(mapa)
