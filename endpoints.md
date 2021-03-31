<h1 id="ednpoints">Endpoints del servicio</h1>

*   [Endpoints para la aplicacion MCAD](#mcad)<br>
*   [Endpoints para la aplicacion TCA](#tca)<br>
*   [Endpoints para la aplicacion Cotejo](#cotejo)<br>

**Nota:** Cambiar las etiquetas `<sec>`, `<tipoActa>`, `<shaMCAD>`, `<shaTCA>` y `<ShaCotejo>` por los valores de busqueda.


<br>-Trae toda la base de datos.
```url
https://service-ine-testing.herokuapp.com/historyService
```
<br>-Trae la base de datos filtrada por Tipo de acta.
```url
https://service-ine-testing.herokuapp.com/historyService/filterTipoActa=<tipoActa>
```

<br>-Trae la base de datos filtrada por Tipo de acta y Sec.
```url
https://service-ine-testing.herokuapp.com/historyService/filterSec=<sec>&filterTipoActa=<tipoActa>
```

<br>-Borra solo una acta, la busca por sec y tipo de acta.
```url
https://service-ine-testing.herokuapp.com/upsi/filterSec=<sec>&filterTipoActa=<tipoActa>
```
<br>-Crea una Acta.<br>(es un metodo POST) su estructura es la siguiente:
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
<h2 id="mcad">Endpoints para la aplicacion MCAD</h2>

<br>-Trae un acta filtrada por ShaMCAD.
```url
https://service-ine-testing.herokuapp.com/historyService/filterShaMCAD=<shaMCAD>
```

<br>-Trae todos los datos de terminal MCAD.
```url
https://service-ine-testing.herokuapp.com/terminalMCAD
```


<br>-Trae los datos de terminalMCAD por Tipo de acta.
```url
https://service-ine-testing.herokuapp.com/terminalMCAD/filterTipoActa=<tipoActa>
```


<br>-Trae los datos de terminalMCAD por ShaMCAD.
```url
https://service-ine-testing.herokuapp.com/terminalMCAD/filterShaMCAD=<shaMCAD>
```


<br>-Guarda los datos para registar que ya se aplico la aplicacion de cotejo en una acta.<br>
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

<br>-Actualizar atributo de ShaMCAD
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


<br>-Trae el tipo de acta de un registro mediante shaMCAD.
```url
https://service-ine-testing.herokuapp.com/tipoActabyShaMCAD=<shaMCAD>
```

<br>-Actualiza el campo ShaMCAD y flag de acuerdo al acta.<br>
(es un metodo PUT) su estructura es la siguiente:
```url
https://service-ine-testing.herokuapp.com/terminalMCAD/addShaMCAD
```
```json
{
    "TipoQR": "CAD",
    "Estado": "AGS",
    "Distrito": 1,
    "Seccion": "338",
    "Casilla": "B1",
    "TipoActa": 2,
    "ShaMCAD": "2439oy75roiy8v6"
}
```

<h2 id="tca">Endpoints para la aplicacion TCA</h2>

<br>-Actualiza el campo ShaMCAD de acuerdo al acta.<br>
(es un metodo PUT) su estructura es la siguiente:
```url
https://service-ine-testing.herokuapp.com/terminalTCA/addShaTCA
```
```json
{
    "ShaTCA": "2439oy75roiy8v6"
}
```
<br>-Trae un acta filtrada por ShaTCA.
```url
https://service-ine-testing.herokuapp.com/historyService/filterShaTCA=<shaTCA>
```


<br>-Trae todos los datos para rellenar TCA.
```url
https://service-ine-testing.herokuapp.com/ValuesTCA
```


<br>-Trae todos los datos para rellenar TCA por Tipo de acta y sec.
```url
https://service-ine-testing.herokuapp.com/ValuesTCA/filterSec=<sec>&filterTipoActa=<tipoActa>
```


<br>-Trae todos los datos para rellenar TCA por ShaTCA.
```url
https://service-ine-testing.herokuapp.com/ValuesTCA/filterShaTCA=<shaTCA>
```


<br>-Trae el historial de una acta para saber por cuales terminales TCA ha pasado busqueda por ShaMCAD.
```url
https://service-ine-testing.herokuapp.com/HistoryTCA/filterShaMCAD=<shaMCAD>
```


<br>-Trae el historial de una acta para saber por cuales terminales TCA ha pasado busqueda por ShaTCA.
```url
https://service-ine-testing.herokuapp.com/HistoryTCA/filterShaTCA=<shaTCA>
```


<br>-Guarda los datos para registar que ya se aplico la aplicacion TCA en una acta mediante ShaTCA.<br>(es un metodo PUT) su estructura es la siguiente:
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


<br>-Actualizar atributo de ShaTCA.
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


<h2 id="cotejo">Endpoints para la aplicacion cotejo</h2>

<br>-Trae un acta filtrada por ShaCotejo.
```url
https://service-ine-testing.herokuapp.com/historyService/filterShaCotejo=<shaCotejo>
```


<br>-Trae los datos de terminalCotejo por ShaCojeto.
```url
https://service-ine-testing.herokuapp.com/terminalCotejo/filterShaCotejo=<shaCotejo>
```


<br>-Guarda los datos para registar que ya se aplico la aplicacion de cotejo en una acta.<br>(es un metodo PUT) su estructura es la siguiente:
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


<br>-Actualizar atributo de ShaCotejo.
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
<br>-Actualiza el campo ShaCotejo y flag de acuerdo al acta.<br>
(es un metodo PUT) su estructura es la siguiente:
```url
https://service-ine-testing.herokuapp.com/terminalCotejo/addShaCotejo
```
```json
{
    "ShaCotejo": "2439oy75roiy8v6"
}
```
<br><br>Developed by **Daniel Gloria Florencio** - [dannielgloria](https://github.com/dannielgloria)
