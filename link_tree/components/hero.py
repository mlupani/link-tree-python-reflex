import reflex as rx

def hero() -> rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.avatar(
                    src="https://github.com/shadcn.png",
                    class_name="w-24 h-24 rounded-full"
                ),
                rx.vstack(
                    rx.text("Hello, I'm John Doe", class_name="text-xl font-bold text-white"),
                    rx.text("I'm a software engineer", class_name="text-lg text-white"),
                    rx.text("Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. ", class_name="text-sm text-white"),
                    class_name="text-white"
                ),
                class_name="w-full items-center gap-6 mt-5"
            ),
        ),
    )