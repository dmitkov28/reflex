import json
import folium
import reflex as rx
from folium.plugins.locate_control import LocateControl
import os
from reflex_app.templates import template

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


style = {
    ".map-container > div:first-child > div:first-child": {
        "position": "inherit!important",
    },
}


def html_map():
    m = folium.Map(
        location=(42.6654086, 23.2597745),
        zoom_start=10,
        tiles="OpenStreetMap",
        width="100%",
        height="100%",
    )

    LocateControl(auto_start=True, keepCurrentZoomLevel=True).add_to(m)

    folium.Marker(
        location=[42.6654086, 23.2597745],
        tooltip="Zenobia Baby",
        popup="Zenobia Baby",
        icon=folium.Icon(icon="heart"),
    ).add_to(m)

    with open(os.path.join(ROOT_DIR, "tracks.geojson"), "r") as f:
        sample_route = json.load(f)

    folium.GeoJson(sample_route).add_to(m)

    return rx.html(m._repr_html_(), class_name="h-[100vh] map-container")


@template(route="/route/[route_id]", title="Trails")
def route() -> rx.Component:
    return rx.box(html_map(), width="100%", class_name="h-full", style=style)
