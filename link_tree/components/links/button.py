import reflex as rx

def button(text: str, link: str) -> rx.Component:
    return rx.link(
        rx.center(
                rx.icon("link"),
                rx.text(text),
                class_name="text-white text-lg font-bold px-4 py-2 rounded-md w-full text-center bg-linear-to-t from-sky-500 to-indigo-500 hover:from-green-400 to-blue-500 gap-2"
            ),
            class_name="w-full flex justify-center items-center",
            is_external=True,
            href=link,
        )