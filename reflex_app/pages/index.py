import datetime
from turtle import width
from reflex_app.templates import template
import reflex as rx

images = ["" for x in range(20)]


def card(image_src: str, text: str, subtitle: str, length: str, duration: str):
    return rx.card(
        rx.image(src=image_src, class_name="min-w-[400px] max-h-[200px]"),
        rx.heading(text, weight="medium", size="7", class_name="mt-8"),
        rx.text(subtitle),
        rx.hstack(rx.text(length), rx.text(duration), spacing="6"),
        class_name="cursor-pointer",
    )


@template(route="/", title="Trails")
def index():
    return rx.box(
        rx.heading("Trails", align="center"),
        rx.box(
            rx.box(
                rx.input(placeholder="Search", class_name="w-full", color_scheme="blue"),
                class_name="col-span-5 md:col-span-4",
            ),
            rx.button("Search", class_name="col-span-5 md:col-span-1", color_scheme="blue"),
            class_name="grid grid-cols-5 gap-2 my-8 h-20 items-center",
        ),
        rx.hstack(
            rx.foreach(
                images,
                lambda x: rx.link(
                    card(
                        "https://source.unsplash.com/random/?trail",
                        "Some Route",
                        "Sofia, Bulgaria",
                        "5km",
                        "1h 23m",
                    ),
                    href="/route/123",
                    underline=None,
                    color_scheme="blue"
                ),
            ),
            class_name="flex gap-8 overflow-x-auto max-w-[100%]",
        ),
        rx.box(
            rx.text(
                f"{datetime.datetime.now().year} © All rights reserved",
                size="2",
                align="center",
            ),
            class_name="w-full fixed bottom-5",
        ),
        class_name="max-w-full",
    )
