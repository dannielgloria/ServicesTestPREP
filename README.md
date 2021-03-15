<div align="center">

![python badge](readme_files/python-badge.png)

</div>

-Development of API REST service for the use of end to end tests of the PREP system

-You need to install [python-3.9.2](https://www.python.org/downloads/release/python-392/)

-Install with pip3, for which it is important to be located within the root folder of the repository to execute the following command line

```sh
pip3.8 install -r requirements.txt
```

-To configure the connection of the database with the API it is important to change the values in the "app.py" file

```sh
app.config['MYSQL_DATABASE_USER'] = 'usuario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'contraseña'
app.config['MYSQL_DATABASE_DB'] = 'nombre de la base de datos'
app.config['MYSQL_DATABASE_HOST'] = 'dirección de la base de datos'
```
## Developed by [Daniel Gloria Florencio](https://github.com/dannielgloria)
