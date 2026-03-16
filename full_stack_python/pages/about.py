import reflex as rx
from ..state import State
from ..ui.base import pagina_base


def about_page() -> rx.Component:
    mi_hijo = rx.vstack(
        rx.heading("Sobre la aplicación", size="9"),
        rx.text(
            "Sirve para gestionar tus gastos, ingresos y transferencias",
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