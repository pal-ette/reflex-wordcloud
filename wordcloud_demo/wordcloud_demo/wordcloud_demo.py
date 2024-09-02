"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_wordcloud import wordcloud
from .words import words

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    width: int = 600

    height: int = 300

    max_words: int = 50

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def set_max_words(self, max_words: int):
        self.max_words = max_words


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Test your custom component by editing ",
                rx.code(filename),
                font_size="2em",
            ),
            rx.hstack(
                wordcloud(
                    words=words,
                    max_words=State.max_words,
                    options={
                        "rotations": 2,
                        "rotationAngles": [-90, 0],
                        "fontFamily": "impact",
                    },
                    size=(State.width, State.height),
                ),
            ),
            rx.hstack(
                rx.text(f"height({State.height})"),
                rx.slider(
                    min=200,
                    max=400,
                    default_value=State.height,
                    on_value_commit=State.set_height,
                ),
                width="100%",
            ),
            rx.hstack(
                rx.text(f"width({State.width})"),
                rx.slider(
                    min=400,
                    max=800,
                    default_value=State.width,
                    on_value_commit=State.set_width,
                ),
                width="100%",
            ),
            rx.hstack(
                rx.text(f"max_words({State.max_words})"),
                rx.slider(
                    min=10,
                    max=100,
                    default_value=State.max_words,
                    on_value_commit=State.set_max_words,
                ),
                width="100%",
            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
