
<p align="center">
  <p align="center">    
    <img src="https://github.com/JesusRamirezGamarra/signature/blob/main/public/img/Logo_Negro.png" alt="BFFs" height="250">    
  </p>
  <p align="center">
       CoderHouse - Python
  </p>
</p>

# CH - Django with SQL - Intermediate Python

>Objetivos Generales:
Desarrollar una WEB Django con patrón MVT subida a Github.

>Se debe entregar:
Link de GitHub con el proyecto totalmente subido a la plataforma.
Proyecto Web Django con patrón MVT que incluya:

- Herencia de HTML.
- Por lo menos 3 clases en models.
- Un formulario para insertar datos a todas las clases de tu models.
- Un formulario para buscar algo en la BD
- Readme que indique el orden en el que se prueban las cosas y/o donde están las
funcionalidades.


> Ubicarse sobre Root del proyecto : 

<!-- <details><summary> -->
1) Intalacion Pre requisitos
<!-- </summary> -->
   
   a)   Creando virtual environment : Un entorno virtual es un entorno Python en el que el intérprete Python, las bibliotecas y los scripts instalados en él están aislados de los instalados en otros entornos virtuales, y (por defecto) cualquier biblioteca instalada en un «sistema» Python, es decir, uno que esté instalado como parte de tu sistema operativo.

```bash
python3 -m venv .venv
```

   b)   Activando virtual environment : El entorno virtual creado en el paso previo debe ser activado antes de poder ser utilizada.
```bash
source .venv/bin/activate
```

   c)   Instalando Django : Django es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como modelo–vista–controlador.
```bash
pip install Django
```

   d)   Opcional - Actualizando PIP : pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Muchos paquetes pueden ser encontrados en el Python Package Index (PyPI). Python 2.7.9 y posteriores (en la serie Python2), Python 3.4 y posteriores incluyen pip (pip3 para Python3) por defecto.

   pip es un acrónimo recursivo que se puede interpretar como Pip Instalador de Paquetes o Pip Instalador de Python
```bash
python3 -m pip install --upgrade pip
```
<!-- </details>
<details><summary> -->
1) Generar scaffolding
<!-- </summary>    -->
Es una técnica utilizada por algunos frameworks Modelo–vista–controlador en los cuales el programador puede especificar cómo se puede usar la base de datos de la aplicación. El framework o compilador utiliza esta especificación, junto con plantillas de código predefinidas, para generar el código final que la aplicación puede usar para crear, leer, actualizar y borrar entradas de la base de datos, tratando así las plantillas como un "andamio" sobre el cual construir una aplicación más fuerte.

    ```bash
    proyecto_final/   # Carpeta del sitio web
    manage.py         # Script para ejecutar las herramientas de Django para este proyecto (creadas usando django-admin)
    proyecto_final/   # Carpeta del Sitio web/Proyecto (creada usando django-admin)
    blog/             # Carpeta de la Aplicación (creada usando manage.py)
    ```
   
   a)   Generar Proyecto
    [ver mas](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/skeleton_website)

```bash
django-admin startproject proyecto_final
```
se crea directorio : proyecto_final y podemos ver su contenido

```bash
cd proyecto_final
```

Estructura creada : 
```bash
proyecto_final/
    manage.py
    proyecto_final/
        settings.py
        urls.py
        wsgi.py
```   
 - **settings.py** contiene todos los ajustes del sitio. Es donde registramos todas las aplicaciones que creamos, la localización de nuestros ficheros estáticos, los detalles de configuración de la base de datos, etc.
 - **urls.py** define los mapeos url-vistas. A pesar de que éste podría contener todo el código del mapeo url, es más común delegar algo del mapeo a las propias aplicaciones, como verás más tarde.
 - **wsgi.py** se usa para ayudar a la aplicación Django a comunicarse con el servidor web. Puedes tratarlo como código base que puedes utilizar de plantilla.
 - **manage.py** se usa para crear aplicaciones, trabajar con bases de datos y empezar el desarrollo del servidor web.
   
fuente : developer.mozilla 


   b)   Generar Aplicacion
   [ver mas](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/skeleton_website)
```bash
python manage.py startapp blog
```
se crea directorio : blog 
```bash
cd ..
```
Estructura total creada : 
```bash
proyecto_final/
    manage.py
    proyecto_final/
    blog/
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        __init__.py
        migrations/
```

   c)   Enlazar Aplicacion

La configuracion de las aplicaciones que utilizaremos la podemos encontrar en el el archivo `setting.py` del directorio `proyecto_final`
```python
import os
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]
```
Test Aplicacion por default : 

```bash
pip freeze > requirements.txt 
```
pip freeze retorna una lista de paquetes instalados similar, pero el formato de salida es el requerido por pip install. Una convención común es poner esta lista en un archivo requirements.txt:
[ver mas ](https://docs.python.org/es/3.8/tutorial/venv.html)

```bash
python manage.py runserver
```

<!-- </details>
<details><summary> -->
3) Crear models - Base datos
<!-- </summary> -->
   
   a) Configuracion Base de datos
   [ver mas](https://docs.djangoproject.com/en/4.1/topics/migrations/)

La configuracion de la base de datos que utilizaremos la podemos encontrar en el el archivo `setting.py` del directorio `proyecto_final`
```python   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```   
Ejecutar el comando `check` para examinar por cualqueir problema en el proyecto : `blog` y `proyecto_final` puede tener antes de aplicar las migraciones ni tocar la base de datos.
```bash
python manage.py check blog
```
Una vez que confirmamos que no existen problemas podemos proceder a ejecutar el comando `migrate` que toma todas las migraciones que no se aplicaron (Django lleva registro de cuáles se aplicaron usando una tabla especial en la base de datos llamada django_migrations) y las corre contra la base de datos - esencialmente, sincroniza el esquema de la base de datos con los cambios hechos a nuestros modelos.
[ver mas](https://djangotutorial.readthedocs.io/es/1.8/intro/tutorial01.html)

```bash
python manage.py migrate
```
   b) Creacion de `Models.py` (modelo) para la Base de datos
Dentro del archivo `models.py` del directorio `blog`, importaremos de  `get_user_model` que es una función auxiliar de Django que obtiene el modelo de Usuario para el proyecto. [ver mas](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

Todoel modelo lo creamos en bae a nuestra definicion [ver mas](https://lucid.app/lucidchart/93ae16ca-54d5-4ec0-9ffe-033ef12cd800/edit?viewport_loc=72%2C154%2C1463%2C655%2C0_0&invitationId=inv_d94e917e-f10e-4379-9710-3e60c3786974#)

<p align="center">    
    <img src="./public/img/EntidadRelacion.png" alt="Modelo entidad relacion" height="350">    
</p>

```python
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
		
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title    

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title    
```
Instalamos pillow para poder utilizar ImageField .[ver mas](https://www.geeksforgeeks.org/imagefield-django-models/)
```
python -m pip install Pillow
```
   c) Migracion de `Models.py` (modelo) y generacion de tablas en la Base de datos

Podemos siempre realizar un check com vimos pasos previos para revizar que no existan errores ante de proceder a generar un script de migracion ( generador de models )

El comando makemigrations crea (pero no aplica) las migraciones para todas las aplicaciones instaladas en tu proyecto (también puedes especificar el nombre de una aplicación para ejecutar una migración para un sólo proyecto). Ésto te da la opoortunidad de comprobar el código para estas migraciones antes de que se apliquen — cuando seas un experto en Django ¡podrás elegir modificarlos ligeramente!


```bash
python manage.py check blog
python manage.py makemigrations
```
podemos visualiar el script de migracion autogenerado por Django utilizando el comando `sqlmigrate` 
```bash
python manage.py sqlmigrate blog  0001
```
para migrar el modelo a la base de datos que tenemos configurada volver a recurirr al comando `migrate`.El comando `migrate` aplica realmente las migraciones a tu base de datos (Django lleva la cuenta de cuáles han sido añadidas a la base de datos actual). 

!importante : se puede utilizar pyclean . para eliminar los directorios __pycache__ , este comando es de mucha utilidad cuando se procede a re crear el modelo y ya existen tablas con datos que puede o no contener campos ( columnas ) con datos obligatorios . Como django genera difernciales esto puede generar problemas.
```bash
python manage.py migrate
```

<!-- </details>
<details><summary> -->
4) Configuracion de Administracion
<!-- </summary> -->
   a) Creamos el admnistrador y configuramos datos base
```bash
python manage.py createsuperuser
```
Completamos la informacion para la creacion del usuario administrador en este caso se ingreso :
```bash
Username (leave blank to use 'jesus'): admin
Email address: luciojesusramirezgamarra@gmail.com
CoderHouse2022
```
   b) Probamos el administador 
Ejecutar el comando runserver para visualizar el adminitrador del blog y acceder utilizando los datos previamente configurados sobre la ruta : http://127.0.0.1:8000/admin/logout/
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/django_admin_login.png" alt="django Admin" height="250">    
</p>

Tras ingresar las credenciales podemos ingresar al modulo de administracion de django el cual es generador por default con ciertas funcionales base que nos ayudaran a configurar el blog.
<p align="center">    
    <img src="./public/img/django_admin.png" alt="django Admin" height="250">    
</p>
<!-- </details>
<details><summary> -->
5) Static Files y Templates

[ver mas](https://docs.djangoproject.com/en/4.0/topics/templates/)
<!-- </summary>    -->
   a) Creamos directorios directamente desde el IDE de visual code, desde nuestro sistema operativo o a traves del comando mkdir sobre las rutas que sean requeridas hasta obtener 
```
    mkdir templates
```
<p align="center">    
    <img src="./public/img/django_staticfiles_templates.png" alt="django Static Files and Templates" height="350">    
</p>

   b) Sobre `setting.py` del directorio `proyecto_final` agregamos la direccion de `DIRS` apuntando al directorio `templates` que creamos previamente.
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
   c) Sobre `setting.py` del directorio `proyecto_final` agregamos las rutas requeridos para los directorios que contendran los archivos statics del proyecto ( imagenes, css, javascript, etc)
```python
STATICFILES_DIRS = [
    # BASE_DIR  /"statics"
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = os.path.join(BASE_DIR, "static/media/") 
STATIC_ROOT = os.path.join(BASE_DIR, "static/static_cdn/")  
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media_cdn/")  
```



<!-- </details>
<details><summary> -->
6) creando views

Una View es un lugar donde ponemos la "lógica" de nuestra aplicación. Pedirá información del modelo que has creado antes y se la pasará a la plantilla . Crearemos una plantilla en el próximo capítulo.
[ver mas](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Generic_views)
<!-- </summary>    -->
   a) Sobre `setting.py` del directorio `proyecto_final` agregamos
```python
from django.shortcuts import render
from .models import Post, Category, Author

def homepage(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'homepage.html', context)
```
   b) Sobre `urls.py` del directorio `proyecto_final` agregamos el importa al view que creamos y la url correspondiente, 
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from blog.views import homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', homepage, name = 'homepage'),
]
```

   c) Sobre `templates`  agregamos un template para realizar la prueba del avance el cual llamaremos `base.html` 

!importante :  vamos a utilizar tailwindcss [ver mas](https://tailwindcss.com/) como libreria alternativa a boostrap [ver mas](https://getbootstrap.com/) para realizar la configuracion y conocer mas sobre esta accediendo a [ver mas](https://tailwindcss.com/docs/installation/play-cdn)

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hola coderHouse Python Django ...
  </h1>
</body>
</html>
```
Ejecutar el servidor y confirmamosque podamos ver el pagina de incio .
```bash
python manage.py runserver
```

<p align="center">    
    <img src="./public/img/BaseHtml.png" alt="django Static Files and Templates" height="150">    
</p>

<!-- </details>
<details><summary> -->
7) Herencia de template

   a) Sobre `urls.py` del directorio `proyecto_final`  agregamos el import a static y el cambio de cadenas utilizando las constantes previamente configuradas en `settings.py`

```python
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```
!importante :  vamos a utilizar JS alpino [ver mas](https://alpinejs.dev/start-here) como libreria alternativa a jquery [ver mas](https://jquery.com/) para poder trabajar la parte dinamica.

```python
{% load static %}
<!doctype html>
<html>
  <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          animation: {
            type: 'type 2.7s ease-out .8s infinite alternate both',
          },
          keyframes: {
            type: {
              '0%': { transform: 'translateX(0ch)' },
              '5%, 10%': { transform: 'translateX(1ch)' },
              '15%, 20%': { transform: 'translateX(2ch)' },
              '25%, 30%': { transform: 'translateX(3ch)' },
              '35%, 40%': { transform: 'translateX(4ch)' },
              '45%, 50%': { transform: 'translateX(5ch)' },
              '55%, 60%': { transform: 'translateX(6ch)' },
              '65%, 70%': { transform: 'translateX(7ch)' },
              '75%, 80%': { transform: 'translateX(8ch)' },
              '85%, 90%': { transform: 'translateX(9ch)' },
              '95%, 100%': { transform: 'translateX(11ch)' },
            },
          },
        }
      }
    }
  </script>
  <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
  </head>
  <body>

      <img src='{% static "./img/dummy.png" %}'/>
  </body>
  </html>
  ```
Ejecutar el servidor y confirmamosque podamos ver el pagina de incio .
```bash
python manage.py runserver
```
  
<p align="center">    
    <img src="./public/img/HomePage_withStaticFile.png" alt="django Static Files and Templates" height="350">    
</p>
   

> Nota : 

* Usar .venv : https://learn.microsoft.com/en-us/windows/python/web-frameworks
* Comando para re ordenar codigo : black .
* Comando para instalar libreria que permite eliminar archivo __Pycache__ : pip install pyclean
* comando para visualizar estructura de directorios : tree -L 2
* comando Breakpoint : https://www.python-engineer.com/posts/python-debugger-and-breakpoint/
  
    - [x] h (elp): Print the list of available commands

    - [x] l (ist): List source code for the current file

    - [x] w (here): Print a stack trace, with the most recent frame at the bottom

    - [x] q (uit): Quit from the debugger

    - [x] p expression: Evaluate the expression in the current context and print its value

    - [x] n (ext): Continue execution until the next line in the current function is 
    reached or it returns (The difference between next and step is that step stops inside a called function, while next executes called functions, only stopping at the next line in the current function)

    - [x] s (tep): Execute the current line, stop at the first possible occasion (either 
    in a function that is called or on the next line in the current function)

    - [x] c (ontinue): Continue execution, only stop when a breakpoint is encountered

* Many-to-many relationships :  https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/


https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks


https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams