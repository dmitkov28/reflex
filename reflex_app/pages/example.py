import random
import reflex as rx
from reflex_app.templates import template


@template(route="/example", title="My Beautiful App")
def example() -> rx.Component:

    class MyCounter(rx.State):
        count: int = 100
        random_number: int | None = None

        def increment(self):
            self.count += 1

        def decrement(self):
            self.count -= 1

        def generate_random_number(self):
            self.random_number = random.randint(1, 1000)    

    def counter_component():
        return rx.flex(
            rx.button(
                "My Decrement",
                color_scheme="red",
                on_click=MyCounter.decrement,
            ),
            rx.heading(MyCounter.count),
            rx.button(
                "My Increment",
                color_scheme="grass",
                on_click=MyCounter.increment,
            ),
            spacing="3",
        )

    def random_number_component():
        return rx.box(
            rx.flex(
                rx.heading(MyCounter.random_number),
                rx.button(
                    "Generate Random Number",
                    color_scheme="red",
                    on_click=MyCounter.generate_random_number(),
                ),
            ),
            margin="40px auto",
        )

    return rx.box(
        rx.vstack(
            rx.text("Hello World!"),
            rx.text("Hello Again, World!", weight="bold", align="center"),
            rx.button(
                "Click me",
                color_scheme="blue",
                size="4",
                on_click=rx.window_alert("Clicked!!!!!"),
            ),
            counter_component(),
            random_number_component(),
        ),
        width="100%",
    )
