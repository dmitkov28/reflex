"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
border = f"1px solid {rx.color('gray', 6)}"
text_color = rx.color("gray", 11)
accent_text_color = rx.color("accent", 10)
accent_color = rx.color("accent", 1)
hover_accent_color = {"_hover": {"color": accent_text_color}}
hover_accent_bg = {"_hover": {"background_color": accent_color}}
content_width_vw = "90vw"


template_page_style = {
    "padding_top": "2em",
    "padding_x": ["auto", "2em"],
    "flex": "1",
    "min_height": "100vh",
}

template_content_style = {
    "border_radius": border_radius,
    "padding": "1em",
}

link_style = {}

overlapping_button_style = {
    "background_color": "white",
    "border_radius": border_radius,
}

markdown_style = {
    "code": lambda text: rx.code(text, color_scheme="gray"),
    "codeblock": lambda text, **props: rx.code_block(text, **props, margin_y="1em"),
}
