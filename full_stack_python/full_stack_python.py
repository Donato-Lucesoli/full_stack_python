"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"
    click = "Hiciste click!"
    navbar_escondido = True


    def cambiar_titulo_input(self, val):
        self.label = val

    def hacer_click(self):
        print(self.click)

    def esconder_aparecer_navbar(self):
        self.navbar_escondido = not self.navbar_escondido


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button("Sign Up", size="3", variant="outline"),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg", width="2em", height="auto", border_radius="25%"
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )


# Dentro de esta función estarán los elementos básicos de todas las páginas
# Con -> rx.Component se dice que la función debe ser un componente de Reflex
# child: rx.Component se refiere al contenido y a rx.vstack
def pagina_base(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.container(
        # Si la variable de estado navbar_escondido es verderdadera navbar() se renderiza, sino no
        rx.cond(
            State.navbar_escondido,
            rx.fragment(),
            navbar(),
        ),
        child,
        rx.color_mode.button(position="top-right"),
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return pagina_base(
        rx.vstack(
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
        ),
    )


app = rx.App()
app.add_page(index)
