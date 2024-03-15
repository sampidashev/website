from rxconfig import config
import reflex as rx

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Hello, I'm Samuel Pidashev!", size="9"),
            rx.text("On an Epic Journey To learn Reflex"),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)