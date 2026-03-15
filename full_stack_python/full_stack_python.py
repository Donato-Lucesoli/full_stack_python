"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import pagina_base
from .state import State
from . import pages

def index() -> rx.Component:
    # Welcome Page (Index)
    mi_hijo = rx.vstack(
        rx.heading(State.label, size="9"),
        rx.text(
            "Get started by editing ",
            rx.code(f"{config.app_name}/{config.app_name}.py"),
            size="5",
        ),
        rx.input(
            default_value=State.label,
            on_click=State.hacer_click,
            on_change=State.cambiar_titulo_input
        ),
        rx.button(
            "Mostrar / Esconder Navbar",
            on_click=State.esconder_aparecer_navbar
        ),
        rx.link(
            rx.button("Check out our docs!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center"
    )
    return pagina_base(mi_hijo)


app = rx.App()
app.add_page(index)
app.add_page(pages.acerca_de_la_app, route="/acerca")
app.add_page(pages.precios, route="/precios")