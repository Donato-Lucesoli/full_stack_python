import reflex as rx
from . import navigation


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

    def redirigir_acerca(self):
        return rx.redirect(navigation.routes.ACERCA_ROUTE)