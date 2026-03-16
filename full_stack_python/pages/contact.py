import reflex as rx
from ..state import State
from ..ui.base import pagina_base
from .. import navigation

@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    mi_hijo = rx.vstack(
        rx.heading("Contacto", size="9"),
        rx.text(
            "Contactese",
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