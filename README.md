# Link Tree App

Una aplicación web construida con Reflex (Python) que permite crear y gestionar enlaces de forma organizada.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clona el repositorio** (si no lo has hecho ya):
```bash
git clone <url-del-repositorio>
cd link_tree
```

2. **Instala las dependencias**:
```bash
pip install -r requirements.txt
```

## Ejecutar la Aplicación

1. **Inicia la aplicación en modo desarrollo**:
```bash
reflex run
```

2. **Abre tu navegador** y ve a:
```
http://localhost:3000
```

## Comandos Útiles

- **Modo desarrollo**: `reflex run`
- **Construir para producción**: `reflex export`
- **Limpiar cache**: `reflex init --force`

## Estructura del Proyecto

```
link_tree/
├── assets/          # Archivos estáticos (favicon, imágenes)
├── link_tree/       # Código principal de la aplicación
│   ├── components/  # Componentes de la interfaz
│   ├── globals.py   # Configuración global
│   └── link_tree.py # Archivo principal de la app
├── requirements.txt # Dependencias de Python
└── rxconfig.py     # Configuración de Reflex
```

## Tecnologías

- **Reflex**: Framework web de Python
- **Python**: Lenguaje de programación principal
- **CSS**: Estilos y diseño

## Desarrollo

Para contribuir al proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## Licencia

Este proyecto está bajo la Licencia MIT.
