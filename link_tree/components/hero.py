import reflex as rx

def hero() -> rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.avatar(
                    src="profile.jpg",
                    class_name="w-24 h-24 rounded-full"
                ),
                rx.vstack(
                    rx.text("Hola, Soy Miguel Angel Lupani", class_name="text-xl font-bold text-white"),
                    rx.text("Soy un ingeniero de software", class_name="text-lg text-white"),
                    rx.text("Desarrollador Senior Full Stack con más de 12 años de experiencia integrando soluciones web, backends robustos y automatización/DevOps. Me especializo en IA aplicada y agentes, trabajando con tecnologías modernas como GPT-4, Ollama y RAG conectado a bases vectoriales. En backend trabajo principalmente con Node.js (Nest.js, Express.js) y PHP (Laravel); en frontend con React/Next.js y Astro. Siempre estoy en busca de retos profesionales y me considero autodidacta, dedicando tiempo diario a aprender para ser un mejor profesional en el área.", class_name="text-sm text-white"),
                    class_name="text-white"
                ),
                class_name="w-full items-center gap-6 mt-5"
            ),
        ),
    )