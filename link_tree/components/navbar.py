import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
            rx.text(
                'Miguel Angel Lupani',
                class_name="text-white"
            ),
            rx.spacer(),
            rx.text(
                'Dev',
                class_name="text-white"
            ),
            rx.text(
                'Sr.',
                class_name="text-white"
            ),
                class_name="w-full text-white",
            )
        ),
        class_name="sticky top-0 z-50 bg-linear-to-t from-sky-500 to-indigo-500"
    )