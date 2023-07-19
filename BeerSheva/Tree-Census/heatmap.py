import folium
from folium.plugins import HeatMap

def create_heatmap(data):
    # create a heat map
    heatmap = folium.Map(location=[31.2517, 34.7912], zoom_start=13)

    # create a heat map layer
    heatmap_layer = HeatMap(data)

    # add the layer to the map
    heatmap_layer.add_to(heatmap)

    # save the map
    heatmap.save('heatmap.html')

    return heatmap