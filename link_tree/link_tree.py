import reflex as rx
from .components.navbar import navbar
from .components.hero import hero
from .components.links.links import links
from .components.footer import footer
from .globals import GENERAL_FONT, STYLESHEETS

def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        links(),
        footer()
    )


app = rx.App(
    style=GENERAL_FONT,
    stylesheets=STYLESHEETS,
)
app.add_page(index)
