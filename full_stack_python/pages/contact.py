import reflex as rx
from ..state import State
from ..ui.base import pagina_base
from .. import navigation
import asyncio


class ContactEntryModel(rx.Model, table=True):
    full_name: str
    email: str
    message: str


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False


    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get("first_name") or ""
        return f"Gracias por tu mensaje {first_name}".strip() + "!"


    @rx.event
    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        data_copy = {}

        for key, value in form_data:
            if value == "" or value is None:
                continue
            else:
                data_copy[key] = value
        print(data_copy)
        
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **data_copy
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield

        # Agregamos un límite de aparición
        await asyncio.sleep(3) 
        self.did_submit = False
        yield

@rx.page(
    route=navigation.routes.CONTACT_ROUTE
    )
def contact_page() -> rx.Component:
    my_form = rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(placeholder="First Name", name="first_name", required=True, width="100%"),
                rx.input(placeholder="Last Name", name="last_name", required=True, width="100%"),
                width="100%"
            ),
            rx.input(placeholder="Email", name="email", type="mail", required=True, width="100%"),
            rx.text_area(placeholder="Tu mensaje", name="mensaje", required=True, width="100%"),
            rx.button("Submit", type="submit"),
            align="center"
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
    ),

    mi_hijo = rx.vstack(
        rx.button(
            "Mostrar / Esconder Navbar",
            on_click=State.esconder_aparecer_navbar
        ),
        rx.heading("Contacto", size="9"),
        rx.cond(ContactState.did_submit, ContactState.thank_you.to_string(), ""),
        rx.desktop_only(
            rx.box(
                my_form,
                width="50vw",
            ),
        ),
        rx.tablet_only(
            rx.box(
                my_form,
                width="75vw"
            ),
        ),
        rx.mobile_only(
            rx.box(
                my_form,
                width="85vw"
            ),
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center"
    )
    return pagina_base(mi_hijo)