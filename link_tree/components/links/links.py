import reflex as rx
from .button import button

def links() -> rx.Component:
    return rx.box(
        rx.container(
            rx.text("Enlaces", class_name="text-white text-2xl font-bold mb-2"),
            rx.vstack(
                button("Proyectos", "https://www.mlupani.vercel.app"),
                button("Linkedin", "https://www.linkedin.com/in/miguel-angel-lupani-5847b720a/"),
                button("Github", "https://github.com/mlupani"),
                button("Instagram", "https://www.instagram.com/miguel_lupani/"),
                button("Whatsapp", "https://wa.me/+5491163717386"),
                class_name="flex text-white justify-center items-center"
            ),
        ),
    )