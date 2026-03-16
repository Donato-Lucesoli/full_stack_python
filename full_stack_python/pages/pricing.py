import reflex as rx
from ..state import State
from ..ui.base import pagina_base


def pricing_page() -> rx.Component:
    mi_hijo = rx.vstack(
        rx.heading("Sobre los precios", size="9"),
        rx.text(
            "Estos son nuestros planes y precios",
            size="5",
        ),
        rx.button(
            "Mostrar / Esconder Navbar",
            on_click=State.esconder_aparecer_navbar
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center"
    )
    return pagina_base(mi_hijo)