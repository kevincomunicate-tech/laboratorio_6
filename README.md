Bienvenido al repositorio oficial del Laboratorio 6. Este proyecto marca la fase inicial de ClassroomHub, una aplicación web desarrollada con el framework Django que servirá como base para la implementación progresiva de modelos, persistencia de datos mediante ORM, migraciones y administración de contenidos en los próximos laboratorios.

📋 Tabla de Contenidos

Características del Proyecto

Estructura del Proyecto

Ciclo de Vida de una Petición HTTP

Requisitos Previos

Instalación y Configuración

Ejecución del Servidor de Desarrollo

Decisiones Técnicas y Buenas Prácticas

Planes Futuros

🚀 Características del Proyecto

Navegación Completa: Implementación funcional de las 3 páginas principales del sistema ClassroomHub.

Arquitectura MVT: Separación clara de responsabilidades entre Modelo, Vista y Plantilla.

Herencia de Plantillas (DRY): Utilización de una plantilla base (base.html) para evitar la duplicación de código HTML y mantener la uniformidad visual.

Enrutamiento Estructurado: Mapeo modular y explícito de URLs en la aplicación.

📁 Estructura del Proyecto

laboratorio_6/
├── classroomhub/           # Configuración global del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Configuración del entorno, apps y plantillas
│   ├── urls.py             # Enrutador principal del proyecto
│   └── wsgi.py             # Entrada WSGI para servidores web
├── main/                   # Aplicación principal de ClassroomHub
│   ├── migrations/         # Directores de migraciones de BD
│   ├── templates/          # Plantillas HTML
│   │   ├── base.html       # Plantilla base con bloques extensibles
│   │   ├── home.html       # Vista de Inicio
│   │   ├── courses.html    # Vista de Cursos
│   │   └── about.html      # Vista de Información
│   ├── __init__.py
│   ├── admin.py            # Configuración del panel de administración
│   ├── apps.py
│   ├── models.py           # Definición de modelos (Preparado para la fase 2)
│   ├── tests.py            # Pruebas unitarias reproducibles
│   ├── urls.py             # Rutas internas de la app
│   └── views.py            # Vistas que gestionan la lógica de negocio
├── .gitignore              # Exclusión de entornos virtuales y archivos sensibles
├── manage.py               # Script de administración de Django
├── README.md               # Documentación del proyecto
└── requirements.txt        # Lista de dependencias


🔄 Ciclo de Vida de una Petición HTTP en ClassroomHub

El recorrido que realiza una solicitud dentro de la arquitectura de ClassroomHub se detalla a continuación:

[Usuario/Navegador] 
       │  petición HTTP GET /cursos/
       ▼
[urls.py (Proyecto)] ───► Resolutor principal redirige hacia la App.
       │
       ▼
[urls.py (App)] ────────► Encuentra el patrón de ruta y llama a 'views.cursos_view'.
       │
       ▼
[views.py] ─────────────► Procesa la lógica de negocio, construye el diccionario de contexto.
       │
       ▼
[Templates] ────────────► Compila 'courses.html' extendiendo de 'base.html' con el contexto.
       │
       ▼
[Respuesta HTTP 200] ───► Devuelve el HTML renderizado al cliente.


🛠️ Requisitos Previos

Asegúrate de tener instalados los siguientes componentes en tu sistema antes de comenzar:

Python: 3.10 o superior (python --version)

Git: Para el control de versiones (git --version)

pip: Gestor de paquetes de Python (pip --version)

⚙️ Instalación y Configuración

Sigue estos pasos para clonar e instalar el proyecto en tu máquina local:

1. Clonar el repositorio

git clone https://github.com/kevincomunicate-tech/laboratorio_6.git
cd laboratorio_6


2. Crear y activar un entorno virtual

En Linux/macOS:

python3 -m venv .venv
source .venv/bin/activate


En Windows (PowerShell):

python -m venv .venv
.venv\Scripts\Activate.ps1


3. Instalar dependencias

pip install -r requirements.txt


🖥️ Ejecución del Servidor de Desarrollo

Una vez instaladas las dependencias, inicia el servidor local ejecutando:

python manage.py runserver


Abre tu navegador e ingresa a la siguiente dirección para verificar el funcionamiento:
👉 http://127.0.0.1:8000/

🧠 Decisiones Técnicas y Buenas Prácticas

Principio DRY (Don't Repeat Yourself): Se implementó base.html integrando la barra de navegación, el pie de página y los scripts compartidos, logrando que cada página secundaria extienda de esta base sin duplicación de código.

Escalabilidad del Enrutamiento: Se utilizó la función include() en el urls.py principal para desacoplar el enrutamiento general de la lógica interna de la aplicación main.

Manejo del Entorno: Se mantuvieron excluidos del repositorio los archivos de entorno virtual (.venv) y la base de datos temporal SQLite mediante .gitignore.

🔮 Planes Futuros (Próximos Laboratorios)

ClassroomHub continuará evolucionando en las siguientes fases:

Fase 2: Definición e implementación de modelos de base de datos (Estudiante, Curso, Profesor).

Fase 3: Migraciones y persistencia mediante ORM de Django en SQLite/PostgreSQL.

Fase 4: Administración de usuarios y operaciones CRUD desde la interfaz y el panel /admin.

✍️ Desarrollado por: Kevin Comunicate Tech — Laboratorio 6
