# ArtBlog Creations

Aplicación web desarrollada con Django para la publicación y gestión de obras de arte.

ArtBlog Creations permite a los usuarios registrarse, iniciar sesión y compartir publicaciones relacionadas con arte, incluyendo información de la obra y una o varias imágenes.

El proyecto implementa autenticación, autorización, validación de formularios, gestión de archivos multimedia y administración mediante Django Admin.

---

# Guía rápida de instalación desde cero

Sigue estos pasos para ejecutar **ArtBlog Creations** en un equipo donde el proyecto no haya sido instalado previamente.

## 1. Obtener el proyecto

Descarga o clona el repositorio y accede a la carpeta raíz del proyecto:

```bash
cd ArtBlogCreations
```

## 2. Crear el entorno virtual

**Windows**

```bash
python -m venv venv
```

**Linux/macOS**

```bash
python3 -m venv venv
```

## 3. Activar el entorno virtual

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

## 4. Instalar las dependencias

Con el entorno virtual activado, instala todas las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## 5. Aplicar las migraciones

Crea la base de datos y las tablas necesarias:

```bash
python manage.py migrate
```

## 6. Crear un superusuario

Para acceder al panel administrativo de Django, crea un superusuario:

```bash
python manage.py createsuperuser
```

Completa el nombre de usuario, correo electrónico y contraseña cuando Django lo solicite.

## 7. Verificar la configuración

Comprueba que la configuración del proyecto sea correcta:

```bash
python manage.py check
```

Si todo está configurado correctamente, Django mostrará un mensaje similar a:

```text
System check identified no issues (0 silenced).
```

## 8. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en:

- Sitio principal: `http://127.0.0.1:8000/`
- Panel administrativo: `http://127.0.0.1:8000/admin/`

## 9. Primer uso de la aplicación

Una vez iniciado el servidor, puedes:

1. Registrarte como un nuevo usuario.
2. Iniciar sesión con tu cuenta.
3. Crear publicaciones de arte.
4. Agregar una o varias imágenes a cada publicación.
5. Editar o eliminar únicamente tus propias publicaciones.
6. Acceder al panel administrativo utilizando el superusuario creado.

> **Nota:** La carpeta `media/` se creará automáticamente cuando se suban imágenes a las publicaciones. La carpeta `staticfiles/` se utiliza para recopilar archivos estáticos en un entorno de producción mediante `collectstatic`.

---

## Características principales

- Registro de usuarios.
- Inicio y cierre de sesión.
- Autenticación mediante `django.contrib.auth`.
- Creación de publicaciones de arte. (Proyecto)
- Edición y eliminación de publicaciones propias.
- Asociación de una o varias imágenes a una publicación. (Tareas dentro de un proyecto)
- Visualización de todas las publicaciones.
- Sección de publicaciones propias.
- Vista detallada de cada publicación.
- Validación de datos mediante formularios Django.
- Validación de archivos de imagen.
- Protección CSRF.
- Restricción de acceso mediante `LoginRequiredMixin`.
- Control de permisos según el propietario de la publicación.
- Panel administrativo de Django personalizado.
- Diseño responsive basado en Bootstrap.
- Separación entre archivos estáticos y archivos multimedia.

---

## Tecnologías utilizadas

- Python
- Django
- HTML5
- CSS3
- Bootstrap
- SQLite
- Django Templates
- Django Authentication System

---

## Estructura del proyecto

```text
ArtBlogCreations/
│
├── ArtBlogCreations/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── usuarios/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── publicaciones/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── templates/
│   ├── base.html
|   └── partials/
│       └── ...
│
├── static/
│   └── css/
│       └── styles.css
│
├── media/
│   └── publicaciones/
│       └── ...
│
├── staticfiles/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```
