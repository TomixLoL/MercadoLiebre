# Comandos para crear un proyecto y una aplicación

## Entorno virtual

`pwd`
> Muestra la ruta actual

`python -m venv .venv`
> Crea un entorno virtual llamado `.venv`

`source .venv/bin/activate`
> Activa el entorno virtual en Linux o Mac

`.\venv\Scripts\activate`
> Activa el entorno virtual en Windows

## Dependencias

`pip list`
> Muestra la lista de paquetes disponibles en el entorno virtual

`pip install django`
> Instala Django

`pip install djlint`
> Instala `djLint`, necesario para la extensión `djLint` de `VSCode`

## Proyecto

`mkdir project`
> Crea un directorio llamado `project`

`cd project`
> Cambia de directorio

`django-admin startproject config .`
> Crea un proyecto en el directorio actual, en la carpeta config

## Servidor

`python manage.py runserver`
> Ejecuta el servidor. Para pararlo: control + c (cmd + c en Mac)

## Aplicaciones

`mkdir apps`
> Crea un directorio llamado 'apps' que contendrá las aplicaciones de Django

`cd apps`
> Cambia de directorio para poder crear las aplicaciones

`django-admin startapp nombre_app`
> Crea una nueva aplicación (recuerda registrarla en settings.py)

## Migraciones

`python manage.py makemigrations`
> Crea las migraciones, que son archivos Python encargados de la base de datos

`python manage.py migrate`
> Ejecuta las migraciones, para que se realicen los cambios en la base de datos

`python manage.py createsuperuser`
> Crea un usuario administrador para acceder a 127.0.0.1:8000/admin

## requirements.txt

Este archivo fue creado con el siguiente comando:
`pip freeze >> requirements.txt`

[Volver](../README.md)
