"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import pagina_base
from .state import State
from . import pages, navigation

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
        rx.hstack(
            rx.link(
                rx.button("Acerca de la app, mediante href"),
                href=navigation.routes.ABOUT_ROUTE,
                is_external=False, # is_external = True abre una nueva pestaña
                ),
            rx.button(
                "Acerca de la app, mediante on_click", 
                on_click=State.redirigir_acerca,
                ),
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center"
    )
    return pagina_base(mi_hijo)


app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_ROUTE)
app.add_page(pages.pricing_page, route=navigation.routes.PRICNG_ROUTE)