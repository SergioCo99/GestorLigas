# GestorLigas

## 1. ¿Qué es GestorLigas?
Aplicación web sencilla que permite realizar una gestión de ligas deportivas de distintos deportes, así como los equipos que componen dichas ligas.
Los usuarios pueden crear los "deportes", "ligas" y "equipos" que deseen. Para ello deben estar registrados y haber iniciado sesión, en caso contrario solo podrán ver los datos. Estos elementos creados por los usuarios, serán visibles para todas las personas que accedan a la página web.

Además pueden consultar, imprimir o guardar como PDF la información sobre los todos equipos de la NBA. Tambíen se puede ver la información de los equipos del All Star de la NBA, es decir, los jugadores que componen el quinteto inicial y unas gráficas con las votaciones obtenidas por cada uno de los integrantes del equipo.


## 2. Software que se necesita instalar

* Para editar código se puede utilizar cualquier editor de texto, yo he usado Visual Studio Code.
* Navegador web para acceder a la parte cliente, por ejemplo, Google Chrome.
* MySQL Workbench, para la administración de la base de datos relacional.
* MongoDBCompass, para la administración de la base de datos no relacional.
* Postman, que nos permite realizar pruebas API.
* Python, la versión que he utilizado ha sido la Python 3.8.5
* Pip, para instalar y administrar paquetes.

## 3. Servicios que hay que arrancar
Clonamos el proyecto en nuestra máquina mediante el siguiente comando:
```
git clone https://github.com/SergioCo99/GestorLigas.git
````
Tambien se puede descargar el proyecto como carpeta zip.

Instalamos las dependencias incluidas en el archivo requirements.txt mediante este comando:
```
pip install -r requirements.txt
````
Una vez instaladas las dependencias, podemos ejecutar el proyecto.

## 4. Dependencias que hay que instalar
Las dependencias a instalar son las que se muestran en el archivo requirements.txt. A continuación se explicarán algunas de ellas.

* Django==3.1.1 -> Framework de desarrollo web de código abierto, escrito en Python.

## 5. Cómo arrancar la parte servidora
Para arrancar el proyecto y poder usarlo mediante el navegador tendremos que ejecutar el siguiente comando:
```
python manage.py runserver
````

Cuando hacemos un cambio que afecta a la base de datos, por ejemplo, en el archivo Models.py que es donde se define la estructura de datos, tenemos que ejecutar los siguientes comandos:

Primero ejecutaremos este comando que se encarga de crear nuevas migraciones en función de los cambios que haya realizado en sus modelos.
```
python manage.py makemigrations
````

El comando anterior crea pero no aplica las migraciones tenemos que usar otro comando. Para aplicar los cambios usaremos "migrate".

```
python manage.py migrate
````

Como este proyecto tiene dos bases de datos, una relacional y otra no relacional, en el comando anterior tenemos que señalar sobre que base de datos queremos ejecutar el comando.

```
python manage.py migrate --database=default
````

```
python manage.py migrate --database=ligainfobd
````

## 6. Cómo acceder a la parte cliente
Para poder visualizar y usar la aplicación web, abriremos un navegador y en la barra superior introduciremos la dirección de localhost puerto 8000, de la siguiente manera:
```
http://127.0.0.1:8000/
````
Para acceder a la parte administradora, cuyo nombre de usuario es "a" y contraseña "a", añadiremos /admin a la dirección anterior:
```
http://127.0.0.1:8000/admin/
````
Como es una aplicación PWA, tambíen podemos descargar la aplicación desde el navegador y poder usarla como una aparente aplicación de escritorio.
