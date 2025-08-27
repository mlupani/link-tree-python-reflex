import reflex as rx
import datetime

def footer() -> rx.Component:
    
    return rx.vstack(
        rx.center(
            rx.text("Footer", class_name="text-white text-sm"),
        ),
        rx.center(
            rx.text(f"Copyright {datetime.datetime.now().year} - All rights reserved", class_name="text-white text-sm"),
        ),
        class_name="w-full absolute bottom-0 z-50 text-white text-center flex justify-center items-center mb-2"
    )