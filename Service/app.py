import time
import json
import pymysql
import datetime
from flask import Flask, request, flash, jsonify
from flaskext.mysql import MySQL

# FLASK Instance my application
app = Flask(__name__)
mysql = MySQL()

##
# Generating the configuration to the connection to the DB
# Change the values of each config according to your credentials from your local DB
##
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '2133010323Gl?'
app.config['MYSQL_DATABASE_DB'] = 'INEDATABASE'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'


mysql.init_app(app)

##
#  Service history endpoints   
##

#* This endpoint gets the full record from the database.
@app.route('/historyService', methods=['GET'])
def get_historyService():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable ORDER BY RAND();')
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint obtains the record by type of act.
@app.route('/historyService?filterTipoActa=<tipoActa>', methods=['GET'])
def get_historyServiceByTipoAct(tipoActa):
    conn = mysql.connect(tipoActa)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE TipoActa = %s;', (tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint obtains the record by type of act and Sec
@app.route('/historyService?filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['GET'])
def get_historyServiceBySecTipoActa(sec,tipoActa):
    conn = mysql.connect(tipoActa)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE Sec = %s AND TipoActa = %s ;', (sec,tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp


##
#  MCAD application endpoints  
##

#* This endpoint gets all the records from the MCAD terminal.
@app.route('/terminalMCAD', methods=['POST', 'GET'])
def get_allMCAD():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT FechaMCADterminal,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable ORDER BY RAND();')
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the MCAD terminal by type of act.
@app.route('/terminalMCAD?filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_allMCADbyTipoActa(tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT FechaMCADterminal,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE TipoActa = %s;', (tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the MCAD terminal by type of record and Sec.
@app.route('/terminalMCAD?filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_allMCADbySecTipoActa(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT FechaMCADterminal,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE Sec = %s AND TipoAct = %s;' (sec,tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the MCAD terminal by type of record, Sec and if the record has an error.
@app.route('/terminalMCAD?filterSec=<sec>&filterTipoActa=<tipoActa>&Error<error>', methods=['POST', 'GET'])
def get_allMCADbySecTipoActaError(sec,tipoActa,error):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT FechaMCADterminal,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE Sec = %s AND TipoAct = %s AND Error = %s;' (sec,tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

##
#  TCA application endpoints  
##

#* This endpoint gets all the records from the TCA terminal.
@app.route('/ValuesTCA', methods=['POST', 'GET'])
def get_allTCA():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable ORDER BY RAND();')
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the TCA terminal by type of act.
@app.route('/ValuesTCA?filterError=<error>', methods=['POST', 'GET'])
def get_allTCAbyError(error):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE Error = %s ORDER BY RAND();',(error))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the TCA terminal by type of record and Sec.
@app.route('/ValuesTCA?filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_RealTCAbySecATipoAct(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;',(sec,tipoActa))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the TCA terminal by type of record, Sec and if the record has an error.
@app.route('/ValuesTCA?filterSec=<sec>&filterTipoActa=<tipoActa>&filterError=<error>', methods=['POST', 'GET'])
def get_RealTCAbySecATipoActAError(sec,tipoActa,error):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s AND Error = %s;',(sec,tipoActa,error))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint creates add a service record to terminal one of the TCA
@app.route('/addTCAt1', methods=['PUT'])
def update_tcaServiceActivityTerminalOne():
    if request.method == 'PUT':
        json_data = request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        ipTCA1 = json_data['IpTCA1']
        fechaTCA1 = datetime.datetime.now()
        usuarioTCA1 = json_data['UsuarioTCA1']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET IpTCA1 = %s ,UsuarioTCA1 = %s , FechaTCA1 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA1,usuarioTCA1,fechaTCA1,sec,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp

#* This endpoint creates add a service record to terminal two of the TCA
@app.route('/addTCAt2', methods=['PUT'])
def update_tcaServiceActivityTerminalTwo():
    if request.method == 'PUT':
        json_data = request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        ipTCA2 = json_data['IpTCA2']
        fechaTCA2 = datetime.datetime.now()
        usuarioTCA2 = json_data['UsuarioTCA2']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET IpTCA2 = %s ,UsuarioTCA2 = %s , FechaTCA2 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA2,usuarioTCA2,fechaTCA2,sec,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp

#* This endpoint creates add a service record to terminal three of the TCA
@app.route('/addTCAt3', methods=['PUT'])
def update_tcaServiceActivityTerminalThree():
    if request.method == 'PUT':
        json_data = request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        ipTCA3 = json_data['IpTCA3']
        fechaTCA3 = datetime.datetime.now()
        usuarioTCA3 = json_data['UsuarioTCA3']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET IpTCA3 = %s ,UsuarioTCA3 = %s , FechaTCA3 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA3,usuarioTCA3,fechaTCA3,sec,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp
    
#* This endpoint creates add a service record to terminal three of the COT
@app.route('/addCOTt1', methods=['PUT'])
def update_cotServiceActivity():
    if request.method == 'PUT':
        json_data = request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        ipCotejo = json_data['IpCotejo']
        fechaCotejo = datetime.datetime.now()
        usuarioCotejo = json_data['UsuarioCotejo']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET IpCotejo = %s ,UsuarioCotejo = %s , FechaCotejo = %s WHERE Sec = %s AND TipoActa = %s ;', (ipCotejo,usuarioCotejo,fechaCotejo,sec,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=3000, debug=True)