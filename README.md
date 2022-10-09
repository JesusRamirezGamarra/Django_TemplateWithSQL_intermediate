
<p align="center">
  <p align="center">    
    <img src="https://github.com/JesusRamirezGamarra/signature/blob/main/public/img/Logo_Negro.png" alt="BFFs" height="250">    
  </p>
  <p align="center">
       CoderHouse - Python
  </p>
</p>

# CH - Django with SQL - Intermediate Python
[Url del Proyecto](https://jesusramirez.pythonanywhere.com/)

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

   b) Configurcion de Template previa a usar extends e include
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
   
<!-- </details>
<details><summary> -->
8) extends e Include
[ver mas](https://docs.djangoproject.com/en/4.1/ref/templates/language/)

   a) extends : Significa que puedes reutilizar partes del HTML para diferentes páginas del sitio web. Las plantillas son útiles cuando quieres utilizar la misma información o el mismo diseño en más de un lugar. para `homepage.html` agregamos al incio del archivo : 

```html
{% extends 'base.html' %}

{% block content %}
```
   b) include : elimina todo el fragmento de la URL que ya ha coincidido hasta ese momento y envía la cadena restante a la URLconf incluida para su procesamiento subsecuente. sobre base.html realizamos el cambio :

```html
  <body>
    {% include "navbar.html" %}
    {% block content %}
    {% endblock content %}
    {% include "footer.html" %}
      <!-- <img src='{% static "img/dummy.png" %}'/> -->
  </body>
```
   c) re Configurando urls.py
   Modificamos las urls para agregarlas donde sobre el proyecto dela aplicacion `blog` donde corresponden para este fin :
   - sobre `url.py` del directorio `proyecto_final`  realmizamos los siguientes cambios :
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# from blog.views import homepage
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', homepage, name = 'homepage'),
    path("blog/",include("blog.urls")),
    path("",include("blog.urls"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
   - creamos `url.py` sobre el directorio `blog`  realmizamos los siguientes cambios :
```python
from django.urls import path
from django.conf import settings

from blog.views import homepage
from django.conf.urls.static import static

urlpatterns = [
    path("",homepage, name = 'homepage'),
]

```

   d) Procedemos a crear los archivos `navbar.html` y `footer.html` en el directorio `templates` por lo pronto no agregamos contenido alguno sobre estos html sin embargo comenzaremos a agregar contenido en ambos archivos y al estar incluidos en `base.html` y todas nuestras paginas a su vez solo se extends de esta pagina procederan a incoporarse en todas 


<!-- </details>
<details><summary> -->
9) Creando el navbar
    
 La barra de navegación es un elemento de la interfaz del usuario dentro de una página web que contiene enlaces a otras secciones del sitio web.

   a) Procedemos crear el navbar tomando como referencia el estilo de tailwind [ver mas](https://tailwindcomponents.com/component/responsive-tailwind-css-navbar)

sobre el archivo `navbar.html` del directorio `templates` agregamos. incluimos `{% load static %}` para poder referenciar a contenido estatico en este caso el logo.
```html
{% load static %}
<header>
<div x-data="{ open: false }" class="relative inline-block text-left">
    <div>
      <button @click="open = ! open" type="button" class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500" id="menu-button" aria-expanded="true" aria-haspopup="true">
        Categories
        <!-- drop-down -->
        <svg class="-mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/>
        </svg>
      </button>
    </div>
  
    <div
      x-show="open"
      x-transition:enter="transition ease-out duration-100"
      x-transition:enter-start="transform opacity-0 scale-95"
      x-transition:enter-end="transform opacity-100 scale-100"
      x-transition:leave="transition ease-in duration-75"
      x-transition:leave-start="transform opacity-100 scale-100"
      x-transition:leave-end="transform opacity-0 scale-95"
      class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
      <div class="py-1" role="none">
<!-- Pendiente Agregar post listados  -->        
      </div>
    </div>
  </div>
</nav>
<!-- searchbar -->
</header>
```
Agregamos un logo y una opcion de menu : HOME , 
```html
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <!-- <svg .... LOGO> -->
            <a href="{% url 'homepage' %}" class="ml-3 text-xl">My blog</a>
        </a>
        <nav class="md:mr-auto md:ml-4 md:py-1 md:pl-4 md:border-l md:border-gray-400	flex flex-wrap items-center text-base justify-center">
            <a href="{% url 'homepage' %}" class="mr-5 hover:text-gray-900 rounded-lg hover:bg-sky-100 inline-flex items-center">Home</a>       
        <!-- Pendiente Agregar mas paginas para el menu  -->                   
```

```

```

   b) Agregamos un search tomando como base el estilo de tailwind [ver mas](https://tailwindcomponents.com/component/search-bar)

Agregamos un search bar para realizar busquedas de post .
```html
<form action ="{% url 'search' %}" class ="search-form"> 
    <div class="pt-2 relative mx-auto text-gray-600">
        <input class="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
        type="text" name="q" placeholder="Search">
        <button type="submit" class="absolute right-0 top-0 mt-5 mr-4">
        <svg class="text-gray-600 h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px"
            viewBox="0 0 56.966 56.966" style="enable-background:new 0 0 56.966 56.966;" xml:space="preserve"
            width="512px" height="512px">
            <path
            d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z" />
        </svg>
        </button>
    </div>
</form>  
```
Sobre el archivo `views.py` sobre el directorio `blog` agregamos una nueva funcion para implementar la busqueda de post . para este fin procedemos a import Q que nos ayudara a realizar querys complejos de forma sencilla. [ver mas](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html)
```python
from django.db.models import Q
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_bar.html', context)

```
Agregamos un nuevo path para poder invocar al search desde el form que agregamos sobre `urls.py` del directorio `blog`

```python
    path('search/', search, name = 'search'),
```

Finalmente creamos una nueva pagina llamada : `search_bar.html` , utilizaremos esta pagina para mostrar el resultado de los post encontrados, y procedemos a extends `base.html` para aprovechar el header y footer que iremos perfeccionando.

```python
{% extends 'base.html' %}
{% block content %}

<section class="blog text-gray-700 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-wrap w-full mb-20 flex-col items-center text-center">
            <h1 class="sm:text-3xl text-2xl font-medium title-font mb-2 text-gray-900"> 
            Search Results
            </h1>        
        </div>



    </div>
</section>      
{% endblock %}
```
Ejecutar el servidor y confirmamosque podamos ver el pagina de incio .
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/Search_post.png" alt="django search post in header" height="200">    
</p>
   


<!-- </details>
<details><summary> -->
10) Configurando Administrador del BLOG
    
[ver mas](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)

   a) configurar `admin.py` del directorio `blog` , procedemos a agregar :

```python
from django.contrib import admin
from .models import Author, Category, Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
```
<p align="center">    
    <img src="./public/img/Admin_Blog.png" alt="django admin blog" height="200">    
</p>

   b) Instalamos markdown :  nos ayuda a formatear el texto para darle un estilo similar a sitios como notion.so . Esto será extremadamente útil para los autores/administradores que coloquen contenido en la página de administración y lo muestren en la interfaz de cómo lo han escrito en lugar de tener que usar html en el backend.

[ver mas](https://learndjango.com/tutorials/django-markdown-tutorial)

```bash
pip install markdown
```
Creamos el directorio : `templatetags` sobre el directorio `blog` y procedemos a crear el archivo `markdown_extras.py`

```python
from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.filter()
@stringfilter


def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])
```
Creamos un nuevo template llamado `post.html` sobre el diretorio `templates` con la estructura :
```python
{% extends 'base.html' %}
{% load markdown_extras %} #<----here

{% block content %}

<div class="py-6">
    {{ post.content | markdown | safe }} #<----here
</div>

{% endblock content %}
```

Ejecutar el servidor y confirmamosque podamos ver el pagina de incio .
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/Search_post.png" alt="django search post in header" height="200">    
</p>
   
<!-- </details>
<details><summary> -->
10) Utilizando markdown_extras para primer Litado de Categorias

   a) sobre el archivo `markdown_extras.py` del directorio `templatetags` del proyecto `blog` vamos a agregar una funciona que nos retorne el lista de categorias [ver mas](https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/)

```python
from blog.models import Category
@register.simple_tag
def get_categories():
    return Category.objects.all()[0:4]
```

   b) sobre el archivo `navbar.html` del directorio `templates` agregamos. incluimos las referencias al markdown_extras para poder invocar a la funcion `get_categories()` y de esta forma acceder al contenido existente en la Base de datos.

```python
{% load markdown_extras %}
{% get_categories as category_list %}
```
Procemos a agregar un Html en un bucle for para poder mostrar un listado en el dropbown de categorias y agregamos item adicional para hacer referencia al `see all post` para mostrar todos los post sin filtrar por categoria.

```html
{% for category in category_list %}
    <a href="" class="text-gray-700 block px-4 py-2 text-sm rounded-lg hover:bg-gray-200 " role="menuitem" tabindex="-1" id="menu-item-0">
    {{ category.title }}
    </a>
{% endfor %}
    <a href="" type="submit" class="text-gray-700 block w-full text-left px-4 py-2 text-sm rounded-lg hover:bg-gray-200" role="menuitem" tabindex="-1" id="menu-item-3">
    See all post</a> 
```
Un paso que es super repetitivo conforme vamos agregando funcionalides resulta el agregar las paginas nuevas sobre `urls.py` tando del directorio `blog` y `proyecto_final`

- `urls.py` en `proyecto_final`
```python
    path("search/",include("blog.urls")),
```
- `urls.py` en `blog`
```python
    from blog.views import homepage,search
    path('search/', search, name = 'search'),
```

Ejecutar el servidor y confirmamosque podamos ver el pagina de incio .
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/DrownList-Categories.png" alt="django DrownList Categories" height="200">    
</p>

   
<!-- </details>
<details><summary> -->
11) Creando post 

   a) Comenzamos agregando las url para las secciones que corresponden sobre el archivo `navbar.html` del directorio `templates` agregamos.

```html
      {% for category in category_list %}
          <a href="{% url 'postlist' category.slug %}" class="text-gray-700 block px-4 py-2 text-sm rounded-lg hover:bg-pink-200 " role="menuitem" tabindex="-1" id="menu-item-0">
          {{ category.title }}
          </a>
      {% endfor %}
        <a href="{% url 'allposts' %}" type="submit" class="text-gray-700 block w-full text-left px-4 py-2 text-sm rounded-lg hover:bg-pink-200" role="menuitem" tabindex="-1" id="menu-item-3">
        See all posts</a> 
```
   b) Creamos `all_posts.html` sobre el directorio `templates` y agregamos como como en otras paginas un extends de `base.html` y hacemos un for para mostrar el `subtitle` , `title` y `overview` de `post`

```html
{% extends 'base.html' %}

{% block content %}

<section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
    
    <div class="flex flex-wrap w-full mb-20">
    <div class="lg:w-1/2 w-full mb-6 lg:mb-0">
        <h1 class="sm:text-3xl text-2xl font-medium title-font mb-2 text-gray-900">
        All posts </h1>
        <div class="h-1 w-20 bg-pink-500 rounded"></div>
    </div>
    </div>
    
    <div class="flex flex-wrap -m-4">
    {% for post in posts %}  
    <div class="xl:w-1/4 md:w-1/2 p-4">
        <div class="bg-gray-100 p-6 rounded-lg">
        <img class="h-50 rounded w-full object-cover object-center mb-6" src="{{ post.thumbnail.url }}" alt="content">
        <h3 class="tracking-widest text-pink-500 text-xs font-medium title-font">
            {{ post.subtitle }}</h3>
        <a href="{% url 'post' post.slug %}" h2 class="text-lg text-gray-900 font-medium title-font mb-4">
            {{ post.title }}</a>
        <p class="leading-relaxed text-base">
            {{ post.overview }}</p>
        </div>
    </div>
    {% endfor %}
    
    </div>
    </div>
</section>
{% endblock content %}
```

   c) para no perder la costumbre no debemos olvidar de agregar la pagina sobre `urls.py` de ambos directorios

- `urls.py` en `proyecto_final`
```python
    path("posts/",include("blog.urls")),
```
- `urls.py` en `blog`
```python
    from blog.views import homepage,search,allposts,post
    path('posts/', allposts, name = 'allposts'),
    path('post/<slug>/', post, name = 'post'),
```

   d)  aprovechamos para agregamos en el post ( claro autores ) en este caso al autor del post , para este fin aprovechamos que en el archivo `post.html` tenemos mucho espacio asi q agregamos ssobre el container un segundo grupo en un `div` para este bloque debajo del post.

```html
{% extends 'base.html' %}
{% load markdown_extras %} 

{% block content %}

<body class="bg-gray-100 font-sans leading-normal tracking-normal"> 
    
    <!--Container-->
	<div class="container w-full md:max-w-3xl mx-auto pt-20 pb-10">
        <div class="w-full px-4 md:px-6 text-xl text-gray-800 leading-normal" style="font-family:Georgia,serif;">

            <!--Title-->
            <div class="font-sans">
                <h1 class="font-bold font-sans break-normal text-gray-900 pt-6 pb-2 text-3xl md:text-4xl">
                {{ post.title }}</h1>
                <p class="text-sm md:text-base font-normal text-gray-600">
                {{ obj.timestamp}}</p>
                <img class="h-50 rounded w-full object-cover object-center mb-6" src="{{ post.thumbnail.url }}" alt="content">
            </div>
            <!--INICIO Post Content-->
            <div class="py-6">
                {{ post.content | markdown | safe }} 
            </div>
            <!--FIN Post Content-->
        </div>     
        
		<!-- INICIO Divider-->
		<hr class="border-b-2 border-gray-400 mb-8 mx-4">
		<!--Author-->
        <h4>Coder post realizado por : </h4>
		<div class="flex w-full items-center font-sans px-4 py-12">

			<img class="w-10 h-10 rounded-full mr-4" src="{{ post.author.profile_picture.url }}">
			<div class="flex-1 px-2">
				<p class="text-base font-bold text-base md:text-xl leading-none mb-2">
				{{ post.author }}</p>
		
			</div>
			
		</div>
		<!--/Author-->
		<hr class="border-b-2 border-gray-400 mb-8 mx-4">        
        <!--FIN Divider-->
    </div>
</body> 

{% endblock content %}
```

   e)  Agregamos lo que mostrara al buscar un blog , esta seccion quedo pendiente porque aun habiamos implementado el `post.html` y tambien porque no habia ingresado utilizando el `back office` de django gracias a la configuracion que realizamos con el administrador la posibilidad de agregar autores,categorias y post.

```html
<!-- inicio : Resultado de busqueda de post -->
<div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4">
    {% for obj in object_list %}
    <div class="p-4 md:w-1/3 md:mb-0 mb-6 flex flex-col justify-center items-center max-w-sm mx-auto">
        <div class="bg-gray-300 h-56 w-full rounded-lg shadow-md bg-cover bg-center" style="background-image: url(https://images.unsplash.com/photo-1521185496955-15097b20c5fe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1951&q=80)"></div>

        <div class=" w-70 bg-white -mt-10 shadow-lg rounded-lg overflow-hidden p-5">
        
        <div class="header-content inline-flex ">
            <div class="category-badge flex-1  h-4 w-4 m rounded-full m-1 bg-purple-100">
            <div class="h-2 w-2 rounded-full m-1 bg-purple-500 " ></div>
            </div>
            {% for category in obj.categories.all %}
            <div class="category-title flex-1 text-sm"> 
            {{ category.title }}
            </div>
            {% endfor %}
        </div>
            <div class="title-post font-medium">
            {{ obj.title }}
            </div>

            <div class="summary-post text-base text-justify">
            {{ obj.overview }}
            </div>
            
            <div class="mt-3">
            <a href="{% url 'post' obj.slug %}" class="bg-blue-100 text-blue-500 rounded p-2 text-sm ">
            Read more
            </a>
        </div>

        </div>
    </div>
    {% endfor %}
    </div>
<!-- fin : Resultado de busqueda de post -->
```
   f)  Agrega sobre `homepage.html` un for para mostrar un listado de post para que no queda totalmente vacio.

```html
<section class="blog text-gray-700 body-font">
<div class="container px-5 py-5 mx-auto">
    <div class="flex flex-wrap w-full mb-20 flex-col items-center text-center">
    <h1 class="sm:text-3xl text-2xl font-medium title-font mb-2 text-gray-900 underline underline-offset-4"> 
        Recent Posts</h1>
    <p class="lg:w-1/2 w-full leading-relaxed text-base">
        These are the most recently added posts</p>
    </div>
    <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4">
    {% for obj in object_list %}
    <div class="p-4 md:w-1/3 md:mb-0 mb-6 flex flex-col justify-center items-center max-w-sm mx-auto">
        <div class="bg-gray-300 h-56 w-full rounded-lg shadow-md bg-cover bg-center" 
        style="background-image: url('{{ obj.thumbnail.url }}')">
    </div>

        <div class=" w-70 bg-white -mt-10 shadow-lg rounded-lg overflow-hidden p-5">
        
        <div class="header-content inline-flex ">
            <div class="category-badge flex-1  h-4 w-4 m rounded-full m-1 bg-purple-100">
            <div class="h-2 w-2 rounded-full m-1 bg-pink-500 " ></div>
            </div>
            {% for category in obj.categories.all %}
            <div class="category-title flex-1 text-sm"> 
                <p class="w-70">{{ category.title }}</p>
            </div>
            {% endfor %}
        </div>
            <div class="title-post font-medium">
            {{ obj.title }}
            </div>

            <div class="summary-post text-base text-justify">
            {{ obj.overview }}
            </div>
            
            <div class="mt-3">
            <a href="{% url 'post' obj.slug %}" class="bg-blue-100 text-black hover:bg-gray-200 rounded p-2 text-sm ">
            Read more
            </a>
        </div>

        </div>
    </div>
    {% endfor %}
    </div>
</div>
</section>
```

- `urls.py` en `proyecto_final`
```python
    path("homepage",include("blog.urls")),
```
- `urls.py` en `blog`
```python
    path("homepage/",homepage, name = 'homepage'),
```
Ejecutar el servidor y confirmamosque podamos ver el pagina de incio .
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/HomePage_RecentPost.png" alt="django HomePage height="300">    
</p>


   g)  Agregamos en `search_bar.html` sobre el directorio `blog` un bucle similar la existente en `homepage.html` pero utilizando el contexto filtrado

```html
<!-- inicio : Resultado de busqueda de post -->
<div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4">
{% for obj in queryset %}
<div class="p-4 md:w-1/3 md:mb-0 mb-6 flex flex-col justify-center items-center max-w-sm mx-auto">

    <div class=" w-70 bg-white -mt-10 shadow-lg rounded-lg overflow-hidden p-5">
        <img class="h-50 rounded w-full object-cover object-center mb-6" src="{{ obj.thumbnail.url }}" alt="content">
        <div class="header-content inline-flex ">
            <div class="category-badge flex-1  h-4 w-4 m rounded-full m-1 bg-purple-100">
            <div class="h-2 w-2 rounded-full m-1 bg-purple-500 " ></div>
            </div>
            {% for category in obj.categories.all %}
            <div class="category-title flex-1 text-sm w-48"> 
                {{ category.title }} 
            </div>
            {% endfor %}
        </div>
        <div class="title-post font-medium">
        {{ obj.title }}
        </div>

        <div class="summary-post text-base text-justify">
        {{ obj.overview }}
        </div>
        
        <div class="mt-3">
        <a href="{% url 'post' obj.slug %}" class="bg-blue-100 text-blue-500 rounded p-2 text-sm ">
        Read more
        </a>
    </div>

    </div>
</div>
{% endfor %}
</div>
<!-- fin : Resultado de busqueda de post -->
```

Ejecutar el servidor y confirmamosque podamos ver el pagina de incio .
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/Search_Post.png" alt="django Search Post Result" height="300">    
</p>

<!-- </details>
<details><summary> -->
11) Creando footer


   a)  Creamos el archivo `footer.html` sobre el directorio `templates` para agregar un `<footer></footer>` que podamos visualizar en todo el `blog` para este fin ya habiamos previamente cuando creamos el archivo `base.html` la consideracion de : `{% include "footer.html" %}`

```html
{% load static %}

<footer id="footer">
    <div >
        <div >
            <h6><a href="https://github.com/JesusRamirezGamarra" target="_blank">Developed by: {{author}} </a></h6>
            <p>Copyright (c) https://github.com/JesusRamirezGamarra  2022  All rights reserved</p>
        </div>
    </div>
    <div  id="centrado">
        <a href="https://github.com/JesusRamirezGamarra" target="_blank" >
            <img id="img" src="{% static 'img/GitHub.png' %}" width="100" >
        </a>
    </div>         
</footer>
```
   b)  Aprovechamos este comportamiento para incluir el llamo a un archivo ubicado en `static` que correponda a `css` el cual ubicaremos en : `static/css` y una imagen con el logo de github ubicado en `static/img`

```css
footer{
    width: 100%;
    height: 66px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffffff;
    background-color: black;
    position: absolute;
    margin:auto;
    position: absolute;
    text-align: center;     
}

#centrado{
    position: absolute;
    left: 0;
    right: 0;
    margin: 0 auto;
    padding-bottom: 120px;
    height: 100px;
    width: 100px;
    bottom: 0px;
}   

footer p {
    font-size:8px;
}


#img{
    position: absolute;
    display: block !important;
    margin-left: auto !important;
    margin-right: auto !important;   
}
```
Ejecutar el servidor y confirmamos que podamos ver el pagina de incio con el footer incorporado
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/footer.png" alt="django footer" height="70">    
</p>

<!-- </details>
<details><summary> -->
13) utilizando Administrador : Donation_Goal, JobGroup, Job

Importante es abordar la importancia del uso de la funcion `__str__` sobre la cual se puede establer consultas complejas para visualizarse en el admninistrador por default [ver mas](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Admin_site)
```python
    def __str__(self):
        job = Job.objects.filter(jobgroup=f"{self.id}")
        return "[    %s  Jobs ]: %s" % (len(job),self.jobgroup)
```


   a)  Creamos sobre `models.py` del directorio `blog`
```python    
class Donation_Goal(models.Model):
    """Objetivo monto total de la donacion con parametros de vigencia"""

    goal = models.IntegerField()
    description = models.CharField(max_length=500)
    startdate = models.DateField()
    enddate = models.DateField()
    active = models.BooleanField()
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s [    Inicio: %s  - Fin:  %s  ]" % (
            self.description,
            self.startdate,
            self.enddate,
        )


class JobGroup(models.Model):
    """Monto : JobGroup para Jobs listado  """

    jobgroup = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # breakpoint()
        # job = Job.objects.filter(jobgroup=f"{self.jobgroup}")
        job = Job.objects.filter(jobgroup=f"{self.id}")
        return "[    %s  Jobs ]: %s" % (len(job), self.jobgroup)
        # return self.jobgroup


class Job(models.Model):
    """Monto : Jobs listado  """

    jobrol = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    jobgroup = models.ForeignKey(JobGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "[    %s  ]: %s" % (self.jobgroup.jobgroup, self.jobrol)
        # return self.jobrol

class Donation(models.Model):
    """Info : del Donante"""

    firtsname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    # jobrol = models.CharField(max_length=40)

    createdate = models.DateTimeField(auto_now_add=True)
    jobrol = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation_Goal = models.ForeignKey(Donation_Goal, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.email)
    
class Collaboration(models.Model):
    """Monto : donado """

    donation = models.IntegerField()
    # jobrol = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.payment, self.createdate)

    
```
   b)  Creamos sobre `admin.py` del directorio `blog`

```python
from .models import Author, Category, Post,Donation_Goal,JobGroup,Job
admin.site.register(Donation_Goal)
admin.site.register(JobGroup)
admin.site.register(Job)
```

realizamos la migracion del modelo creado para actualizar la base de datos.

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

Ejecutar el servidor y confirmamos que podamos ver el pagina de incio con el footer incorporado
```bash
python manage.py runserver
```
<p align="center">    
    <img src="./public/img/Admin_jobPost.png" alt="django footer" height="250">    
</p>



<!-- </details>
<details><summary> -->
14) Formulario : Dona ( donaciones )
    
Permite registra una donacion que corresponde a una Meta registrada desde el administrador.


<!-- </details>
<details><summary> -->
15)  Formulario : Contact ( contactanos )

Permite ingresar consultas y/o sugerencias de parte de cualquier usuarios del blog.

<!-- </details>
<details><summary> -->
16)  Formulario : Embrace ( adopta )

Permite inscribirte en el proceso de adopcion de un PetAmigo (mascota)



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
* FreeHosting for django : https://www.pythonanywhere.com/
* Convert .pnt to .svg : https://www.adobe.com/express/feature/image/convert/png-to-svg
* python manage.py shell : ejecutar comandos python sobre la base de datos

https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks


https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams


lsof -i tcp:8080
kill -9 <PID>