from django.shortcuts import render, redirect
import os
import folium
import geopandas as gpd
from folium import GeoJson

# Create your views here.

def home(request):
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp_Iran')

    m = folium.Map(location=[32.4279, 53.6880], zoom_start=5)
    # style_Iran_road_dd = {'fillColor': '#228B22', 'color': '#228B22'}
    style_Iran_roads = {'color': 'red'}
    style_Iran_water = {'color': 'blue'}

    Iran_road_dd = gpd.read_file(os.path.join(shp_dir, 'Iran_roads.shp'))
    Iran_road_dd_geojson = Iran_road_dd.to_crs("EPSG:4326").to_json()

    Iran_water_dd = gpd.read_file(os.path.join(shp_dir, 'IRN_water_areas_dcw.shp'))
    Iran_water_dd_geojson = Iran_water_dd.to_crs("EPSG:4326").to_json()

    GeoJson(Iran_road_dd_geojson, name='iran_roads', style_function=lambda x: style_Iran_roads).add_to(m)
    GeoJson(Iran_water_dd_geojson, name='iran_water', style_function=lambda x: style_Iran_water).add_to(m)
    
    folium.LayerControl().add_to(m)

    m = m._repr_html_()
    context = {'my_map': m}
    return render(request, 'home.html', context)

