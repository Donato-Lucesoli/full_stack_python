import reflex as rx
from .nav import navbar
from ..state import State


# Dentro de esta función estarán los elementos básicos de todas las páginas
# Con -> rx.Component se dice que la función debe ser un componente de Reflex
# child: rx.Component se refiere al contenido y a rx.vstack
def pagina_base(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment( # fragment no hace nada
        # Si la variable de estado navbar_escondido es verderdadera navbar() se renderiza, sino no
        rx.cond(
            State.navbar_escondido,
            rx.fragment(),
            navbar(),
        ),
        rx.box(
            child,
            padding="1em",
            width="100%",
        ),
        rx.color_mode.button(position="bottom-right"),
    )