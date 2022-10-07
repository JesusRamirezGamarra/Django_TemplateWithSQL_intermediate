
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

1) Intalacion Pre requisitos :
   
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

2) Generar scaffolding :
   
   a) django-admin startproject proyecto_final

   b) cd proyecto_final

   c) python manage.py startapp blog

3) Crear models Base datos :
   
   a)

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