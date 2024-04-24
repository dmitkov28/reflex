"""Welcome to Reflex!."""

# Import all the pages.
from reflex_app.pages import *

import reflex as rx

from reflex_app.pages import example


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()
