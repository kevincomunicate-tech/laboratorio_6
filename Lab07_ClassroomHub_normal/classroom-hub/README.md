# ClassroomHub

ClassroomHub es un portal de recursos de aprendizaje construido con Django.
En el **Laboratorio 6** se crearon las rutas, vistas y plantillas; desde el
**Laboratorio 7** los recursos se guardan en **MariaDB/MySQL**, se consultan con el
ORM y se administran con **Django Admin**.

## Requisitos

- Python 3.12 o superior
- Django 6.1.3 (fijado en `requirements.txt`)
- MariaDB 10.11 o superior, o MySQL 8.4 o superior
- `mysqlclient` y `python-dotenv` (incluidos en `requirements.txt`)

> El proyecto se probó con MariaDB 13.0.2 en Windows (puerto 3307, porque XAMPP
> ocupa el 3306). MariaDB 10.4 de XAMPP **no** es compatible con Django 6.1.

## 1. Crear la base y la cuenta de la aplicación

Con una cuenta administradora del servidor SQL:

```sql
CREATE DATABASE IF NOT EXISTS classroom_hub CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'classroomhub_user'@'127.0.0.1' IDENTIFIED BY 'your_private_password';
GRANT ALL PRIVILEGES ON classroom_hub.* TO 'classroomhub_user'@'127.0.0.1';
GRANT ALL PRIVILEGES ON test_classroom_hub.* TO 'classroomhub_user'@'127.0.0.1';
FLUSH PRIVILEGES;
```

Los permisos se limitan a la base de desarrollo y a la base descartable de pruebas.
La aplicación nunca usa `root`.

## 2. Entorno virtual y dependencias

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Linux:

```bash
sudo apt install python3-venv python3-dev default-libmysqlclient-dev build-essential pkg-config
python3 -m venv .venv-linux
source .venv-linux/bin/activate
python -m pip install -r requirements.txt
```

Un entorno virtual no se puede llevar de un sistema operativo a otro: por eso se usan
`.venv` (Windows) y `.venv-linux` (Linux). Ambos están en `.gitignore`.

## 3. Configuración (`.env`)

Copia `.env.example` como `.env` y escribe la contraseña y el puerto reales:

```text
DB_NAME=classroom_hub
DB_USER=classroomhub_user
DB_PASSWORD=your_private_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

`.env` **no** se sube a Git; `.env.example` sí, porque solo tiene valores de ejemplo.

## 4. Migraciones, superusuario y ejecución

```bash
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

| Ruta | Descripción |
|---|---|
| `/` | Página principal |
| `/resources/` | Catálogo consultado desde la base de datos |
| `/about/` | Información del proyecto |
| `/admin/` | Administración de categorías y recursos |

## 5. Modelos

- `Category`: `name` (único) y `description`.
- `Resource`: `title`, `description`, `available`, `resource_type`, `category`
  (clave foránea con `PROTECT`) y `created_at`.

Migraciones: `0001_initial` crea las tablas y `0002_resource_resource_type`
agrega la columna `resource_type`.

## 6. Pruebas

```bash
python manage.py test pages
```

Diez pruebas con `TestCase`. Django crea y elimina la base `test_classroom_hub`,
así que los datos de `classroom_hub` no se modifican.

## Pendiente

Inicio de sesión propio, formularios públicos, CRUD desde vistas personalizadas y API REST.
