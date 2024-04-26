"""The home page of the app."""

from turtle import width
from reflex_app import styles
from reflex_app.templates import template

import reflex as rx


@template(route="/", title="Trails")
def index() -> rx.Component:
   
    return rx.box(
        rx.heading("Trails", align="center"),
        width="100%"
    )
