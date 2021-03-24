<div align="center">

![python badge](readme_files/python-badge.png)

</div>

Contenido
================
*   [Endpoints del servicio](#ednpoints)
    *   [Endpoints para la aplicacion MCAD](#mcad)
    *   [Endpoints para la aplicacion TCA](#html)
    *   [Endpoints para la aplicacion Cotejo](#cotejo)
    *   [Endpoints para la aplicacion Cotejo](./endpoints.txt)
*   [Configuracion](#settings)
* * *

<h2 id="ednpoints">Endpoints del servicio</h2>

**Nota:** Cambiar las etiquetas `<sec>`, `<tipoActa>`, `<shaMCAD>`, `<shaTCA>` y `<ShaCotejo>` por los valores de busqueda.


-Trae toda la base de datos.
```url
https://service-ine-testing.herokuapp.com/historyService
```
-Trae la base de datos filtrada por Tipo de acta.
```url
https://service-ine-testing.herokuapp.com/historyService/filterTipoActa=<tipoActa>
```

-Trae la base de datos filtrada por Tipo de acta y Sec.
```url
https://service-ine-testing.herokuapp.com/historyService/filterSec=<sec>&filterTipoActa=<tipoActa>
```

-Borra solo una acta, la busca por sec y tipo de acta.
```url
https://service-ine-testing.herokuapp.com/upsi/filterSec=<sec>&filterTipoActa=<tipoActa>
```
-Crea una Acta.<br>(es un metodo POST) su estructura es la siguiente:
```url
https://service-ine-testing.herokuapp.com/createAtc
```
```json
{
    "Sec": 5,
    "Consec": 1,
    "TipoQR": "Movil",
    "Estado": "CDMX",
    "Distrito": 1,
    "Seccion": 1,
    "Casilla": 1,
    "TipoActa": 5,
    "ShaTCA":  "2439oy75roiy8v6",
    "ShaMCAD":  "2439oy75roiy8v6",
    "ShaCotejo":  "2439oy75roiy8v6",
    "IpMCAD": "0.0.0.1",
    "UsuarioMCAD": "nombre.apellido.aplicacion",
    "BolSob": 1,
    "PersVot": 1,
    "RepVot": 1,
    "TotPVnRep": 1,
    "P1": 1,
    "P2": 1,
    "P3": 1,
    "P4": 1,
    "P5": 1,
    "P6": 1,
    "P7": 1,
    "P8": 1,
    "P9": 1,
    "P10": 1,
    "P11": 1,
    "P12": 1,
    "C1": 1,
    "C2": 1,
    "C3": 1,
    "C4": 1,
    "CNoReg": 1,
    "VotNulos": 1,
    "Tot1": 1,
    "Tot2": 1
}
```
<h3 id="mcad">Endpoints para la aplicacion MCAD</h3>

-Trae un acta filtrada por ShaMCAD.
```url
https://service-ine-testing.herokuapp.com/historyService/filterShaMCAD=<shaMCAD>
```

-Trae todos los datos de terminal MCAD.
```url
https://service-ine-testing.herokuapp.com/terminalMCAD
```


-Trae los datos de terminalMCAD por Tipo de acta.
```url
https://service-ine-testing.herokuapp.com/terminalMCAD/filterTipoActa=<tipoActa>
```


-Trae los datos de terminalMCAD por ShaMCAD.
```url
https://service-ine-testing.herokuapp.com/terminalMCAD/filterShaMCAD=<shaMCAD>
```


-Guarda los datos para registar que ya se aplico la aplicacion de cotejo en una acta.<br>
(es un metodo PUT) su estructura es la siguiente:
```url
https://service-ine-testing.herokuapp.com/addMCAD
```
```json
{
    "ShaMCAD": "2439oy75roiy8v6",
    "IpMCAD": "0.0.0.1",
    "UsuarioMCAD": "nombre.apellido.aplicacion"
}
```

-Actualizar atributo de ShaMCAD
```url
https://service-ine-testing.herokuapp.com/updateShaMCAD
```
```json
{
    "Sec": 1,
    "TipoActa": 1,
    "ShaMCAD": "wxec8vibon9ve67n097b468eb6"
}
```


-Trae el tipo de acta de un registro mediante shaMCAD.
```url
https://service-ine-testing.herokuapp.com/tipoActabyShaMCAD=<shaMCAD>
```

<h3 id="tca">Endpoints para la aplicacion TCA</h3>

-Trae un acta filtrada por ShaTCA.
```url
https://service-ine-testing.herokuapp.com/historyService/filterShaTCA=<shaTCA>
```


-Trae todos los datos para rellenar TCA.
```url
https://service-ine-testing.herokuapp.com/ValuesTCA
```


-Trae todos los datos para rellenar TCA por Tipo de acta y sec.
```url
https://service-ine-testing.herokuapp.com/ValuesTCA/filterSec=<sec>&filterTipoActa=<tipoActa>
```


-Trae todos los datos para rellenar TCA por ShaTCA.
```url
https://service-ine-testing.herokuapp.com/ValuesTCA/filterShaTCA=<shaTCA>
```


-Trae el historial de una acta para saber por cuales terminales TCA ha pasado busqueda por ShaMCAD.
```url
https://service-ine-testing.herokuapp.com/HistoryTCA/filterShaMCAD=<shaMCAD>
```


-Trae el historial de una acta para saber por cuales terminales TCA ha pasado busqueda por ShaTCA.
```url
https://service-ine-testing.herokuapp.com/HistoryTCA/filterShaTCA=<shaTCA>
```


-Guarda los datos para registar que ya se aplico la aplicacion TCA en una acta mediante ShaTCA.<br>(es un metodo PUT) su estructura es la siguiente:
```url
https://service-ine-testing.herokuapp.com/addTCA
```
```json
{
    "ShaTCA": "2439oy75roiy8v6",
    "IpTCA": "0.0.0.1",
    "UsuarioTCA": "nombre.apellido.aplicacion",
    "ErrorTCA": "true"
}
```


-Actualizar atributo de ShaTCA.
```url
https://service-ine-testing.herokuapp.com/updateShaTCA
```
```json
{
    "Sec": 1,
    "TipoActa": 1,
    "ShaTCA": "2439oy75roiy8v6"
}
```

<h3 id="cotejo">Endpoints para la aplicacion cotejo</h3>

-Trae un acta filtrada por ShaCotejo.
```url
https://service-ine-testing.herokuapp.com/historyService/filterShaCotejo=<shaCotejo>
```


-Trae los datos de terminalCotejo por ShaCojeto.
```url
https://service-ine-testing.herokuapp.com/terminalCotejo/filterShaCotejo=<shaCotejo>
```


-Guarda los datos para registar que ya se aplico la aplicacion de cotejo en una acta.<br>(es un metodo PUT) su estructura es la siguiente:
```url
https://service-ine-testing.herokuapp.com/addCOT
```
```json
{
    "ShaCojeto": "2439oy75roiy8v6",
    "IpCotejo": "0.0.0.1",
    "UsuarioCotejo": "nombre.apellido.aplicacion"
}
```


-Actualizar atributo de ShaCotejo.
```url
https://service-ine-testing.herokuapp.com/updateShaCotejo
```
```json
{
    "Sec": 1,
    "TipoActa": 1,
    "ShaCotejo": "34wc54v5b6np9n6b9v8"
}
```

<h2 id="settings">Configuracion</h2>
-Desarrollo del servicio API REST para el uso de pruebas end to end del sistema PREP

-Es necesario instalar [python-3.9.2](https://www.python.org/downloads/release/python-392/)

-Instalar con pip3, para lo cual es importante estar ubicado dentro de la carpeta "requirements" para ejecutar

```sh
pip3.8 install -r requirements.txt
```

-To configure the connection of the database with the API it is important to change the values in the "app.py" file

```python
app.config['MYSQL_DATABASE_USER'] = 'usuiario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'contraseña'
app.config['MYSQL_DATABASE_DB'] = 'nombre de la base de datos'
app.config['MYSQL_DATABASE_HOST'] = 'dirección de la base de datos'
```
</br>

Developed by **Daniel Gloria Florencio** - [dannielgloria](https://github.com/dannielgloria)
