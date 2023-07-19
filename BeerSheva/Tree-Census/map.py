import folium

# create a map
m = folium.Map(location=[31.2517, 34.7912], zoom_start=13)

# save the map
m.save('map.html')