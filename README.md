# daily-farming

Herramienta web prototipo usando Django la cual busca apoyar la gestión de cultivos alimentarios a baja escala.

# Autores:

- Carlos Rangel
- David Medina
- Daniel Tamara
- Laura Castaño
- Samuel Falla

# Propósito:

Con esta aplicación web prototipo se busca proporcionar herramientas necesarias para aventurarse en la agricultura a baja escala.
En una interfaz simplificada, podrá construirse un seguimiento de cultivo definido que se ajuste más a las necesidades del usuario.
Gracias a las funcionalidades que se desarrollarán se busca también generar una fuente informativa para que más personas puedan generar sus propios alimentos como algunos de la canasta básica familiar
que no requieran tierras extensas o sistemas especiales y complejos para guiar y optimizar sus producciones personales.

## Despliegue:

### 1. Instalar Python:

Para este proyecto será necesario tener instalado el lenguaje Python en el entorno de desarrollo. Para esto, se recomienda seguir los pasos de la página oficial de Python, según el sistema operativo que se tenga:
https://www.python.org/downloads/

### 2. Crear ambiente virtual:

Se recomienda el uso de ambiente virtual para poder instalar las versiones con las que se desarolló el proyecto para esto se ejecutan los siguiente comandos en la terminal una vez situado en la carpeta del proyecto:

- pip install virtualenv
- python -m venv nombre_ambiente
- .\venv\Scripts\activate (Formato de dirección de Windows) -> Activa en ambiente virtual localmente

### 3. Instalar librerias

Para ahorar pasos y problemas en el versionado de las librerias, se incluyó un archivo .txt el cual se nota como _'requeriments.txt'_, este contiene información de las librerias requeridas para ejecutar el proyecto.
A continuación una breve explicación de las principales librerias incluidas:

### Django:

Framework que estructura todo el proyecto que ayuda a que la aplicación respete el patrón modelo-vista-controlador. Para este caso, se usará el modelo-vista-template el cual sigue siendo soportado. Además de incluir diferentes 'contribs'
integrados como un sistema de auntenticación.

Para inicializar el proyecto, cree una carpeta y después ejecute los siguientes comandos si desea inicializar un proyecto diferente respecto a este:

- django-admin startproject nombre_proyecto

Ahora se generará una carpeta principal de su proyecto, para crear una aplicación nueva dentro del proyecto:

- python manage.py startapp nombre_app

Y posterior, deberá indicar al proyecto que se registró una nueva app. Para esto dirigase a su carpeta principal del proyecto y vaya a _'settings.py'_. Continue a la sección _'INSTALLED_APPS'_ y agrege al final el nombre de su aplicación entre comillas simples junto a una coma: 'nombre_app',

### django-bootstrap4 y django-widget-tweaks

Integración de la libreria bootstrap4 para ser codificado de manera más limpia y mejor mantenida en los templates, manteniendo todo bajo una misma anotación hasta para los estilos predefinidos de boostrap4.

widget-tweaks junto a **django-bootstrap4** ayudará a configurar los estilos en los templates (archivos html) de su proyecto.

### django-environ:

Libreria requerida para poder cargar las variables de entorno que se vayan a usar. **Este proyecto puede ser configurado con una base de datos diferente**, estas variables se podrán ver reflejadas en el archivo _'settings.py'_
de la carpeta principal del proyecto Django.

Cree un archivo .env en la carpeta principal del proyecto (no la raiz) que contenga los siguientes datos que deberá reemplazar:

- DEBUG= _TRUE/FALSE_
- SECRET*KEY= \_KEY_DJANGO*

- DB*NAME= \_NOMBRE_DATABASE*
- DB*USER= \_USUARIO_DATABASE*
- DB*PASSWORD= \_CONTRASEÑA_DATABASE*
- DB*HOST= \_URL_HOST_DATABASE*
- DB*PORT= \_PUERTO_ALOJADO_DATABASE*

También puede utilizarse python-dotenv.

### psycopg2-binary:

Libreria que ayuda a la comunicación de la aplicación con el motor de base de datos PostegreSQL. Puede ser cambiado según el motor con el que desee trabajar.

Se sugiere igualmente especificar el uso de este motor en _'settings.py'_, en la sección _DATABASES_ donde estará _ENGINE_, acá si se desea usar esta libreria se escribirá _django.db.backends.postgresql_psycopg2_

Recuerde que si lo desea ejecutar localmente, deberá instalar PostgreSQL y un gestor de base de datos como PgAdmin4. De otra manera, hacer uso de una base de datos en linea que cuente con este motor:
https://www.postgresql.org/download/

## Configuración del proyecto:

Una vez configuradas las librerias y base de datos. Deberá migrar los modelos necesarios de su aplicación creada para que de esta forma se generen las relaciones respectivas en esta. Si gusta añadir diferentes modelos, dirigase a la aplicación creada _'nombre_app'_ y en _'models.py'_ seguir el formato de modelos de Django por el ORM:
https://docs.djangoproject.com/en/4.2/topics/db/models/

Para ejecutar las migraciones:

- python manage.py makemigrations nombre_app
- python manage.py migrate

Una vez ejecute estos comandos, se migrarán los datos nuevos a su base de datos modificada.

## Iniciar servidor:

Para iniciar el servidor local, si instaló las librerias y configuró este proyecto según haya considerado mejor, deberá ejecutar:

- python manage.py runserver (Recuerde situarse en la carpeta raiz del proyecto en la linea de comandos)
