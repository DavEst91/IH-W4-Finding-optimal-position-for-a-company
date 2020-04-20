import folium

def add_points_to_map(mapa,df,category,dict_colors,radius=100):
    for latitude,longitude,category,name in df[["latitude","longitude",category,"name"]].values:
        folium.Circle(
        radius=radius,
        location=[latitude,longitude],
	fill=True,
	popup=name,
        color=dict_colors[category],).add_to(mapa)
