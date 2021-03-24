<h1 id="settings">Configuracion</h1>
-Desarrollo del servicio API REST para el uso de pruebas end to end del sistema PREP

-Es necesario instalar [python-3.9.2](https://www.python.org/downloads/release/python-392/)

-Instalar con pip3, para lo cual es importante estar ubicado dentro de la carpeta "requirements" para ejecutar

```sh
pip3.8 install -r requirements.txt
```

-Para configurar la conexión de la base de datos con la el servicio de la API es importante cambiar los valores en el archivo "app.py"

```python
app.config['MYSQL_DATABASE_USER'] = 'usuiario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'contraseña'
app.config['MYSQL_DATABASE_DB'] = 'nombre de la base de datos'
app.config['MYSQL_DATABASE_HOST'] = 'dirección de la base de datos'
```
</br>

Developed by **Daniel Gloria Florencio** - [dannielgloria](https://github.com/dannielgloria)