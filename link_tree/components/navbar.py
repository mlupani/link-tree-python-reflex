import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
            rx.link(
                rx.text("Home"),
                href="/",
                class_name="text-white"
            ),
            rx.spacer(),
            rx.link(
                rx.text("About"),
                href="/about",
                class_name="text-white"
            ),
            rx.link(
                rx.text("Contact"),
                href="/contact",
                class_name="text-white"
            ),
                class_name="w-full text-white",
            )
        ),
        class_name="sticky top-0 z-50 bg-linear-to-t from-sky-500 to-indigo-500"
    )