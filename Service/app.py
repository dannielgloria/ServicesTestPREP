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
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '2133010323Gl?'
# app.config['MYSQL_DATABASE_DB'] = 'INEDATABASE'
# app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

app.config['MYSQL_DATABASE_USER'] = 'u917498081_servicedb'
app.config['MYSQL_DATABASE_PASSWORD'] = '$|OS8YaC/r5I'
app.config['MYSQL_DATABASE_DB'] = 'u917498081_INEDATABASE'
app.config['MYSQL_DATABASE_HOST'] = '31.220.104.219'


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
@app.route('/historyService/filterTipoActa=<tipoActa>', methods=['GET'])
def get_historyServiceByTipoAct(tipoActa):
    conn = mysql.connect(tipoActa)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE TipoActa = %s;', (tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint obtains the record by type of act and Sec
@app.route('/historyService/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['GET'])
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

#* This endpoint create an Act to MCAD terminal.
@app.route('/createAtc', methods=['POST'])
def create_atcService():
    if request.method == 'POST':
        json_data = request.get_json()
        sec = json_data['Sec']
        consec = json_data['Consec']
        tipoQr = json_data['TipoQR']
        estado = json_data['Estado']
        distrito = json_data['Distrito']
        seccion = json_data['Seccion']
        casilla = json_data['Casilla']
        tipoActa = json_data['TipoActa']
        shaTCA = json_data['ShaTCA']
        shaMCAD = json_data['ShaMCAD']
        shaCotejo = json_data['ShaCotejo']
        ipMCAD = json_data['IpMCAD']
        usuarioMCAD = json_data['UsuarioMCAD']
        fechaMCAD = datetime.datetime.now()
        bolSob = json_data['BolSob']
        persVot = json_data['PersVot']
        repVot = json_data['RepVot']
        totPVnRep = json_data['TotPVnRep']
        P1 = json_data['P1']
        P2 = json_data['P2']
        P3 = json_data['P3']
        P4 = json_data['P4']
        P5 = json_data['P5']
        P6 = json_data['P6']
        P7 = json_data['P7']
        P8 = json_data['P8']
        P9 = json_data['P9']
        P10 = json_data['P10']
        P11 = json_data['P11']
        P12 = json_data['P12']
        C1 = json_data['C1']
        C2 = json_data['C2']
        C3 = json_data['C3']
        C4 = json_data['C4']
        cNoReg = json_data['CNoReg']
        votNulos = json_data['VotNulos']
        tot1 = json_data['Tot1']
        tot2 = json_data['Tot2']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('INSERT INTO ServiceTable (Sec,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa,ShaTCA,ShaMCAD,ShaCotejo,IpMCAD,UsuarioMCAD,FechaMCAD,BolSob,PersVot,RepVot,TotPVnRep,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s,%s,%s,%s, %s, %s, %s, %s,%s,%s,%s,%s,%s);', (sec,consec,tipoQr,estado,distrito,seccion,casilla,tipoActa,shaTCA,shaMCAD,shaCotejo,ipMCAD,usuarioMCAD,fechaMCAD,bolSob,persVot,repVot,totPVnRep,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,cNoReg,votNulos,tot1,tot2))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp


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
@app.route('/terminalMCAD/filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_allMCADbyTipoActa(tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT IpMCAD,UsuarioMCAD,FechaMCAD,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE TipoActa = %s;', (tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the MCAD terminal by type of record and Sec.
@app.route('/terminalMCAD/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_allMCADbySecTipoActa(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT IpMCAD,UsuarioMCAD,FechaMCAD,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE Sec = %s AND TipoAct = %s;',  (sec,tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

# #* This endpoint gets all the records of the MCAD terminal by type of record, Sec and if the record has an error.
# @app.route('/terminalMCAD/filterSec=<sec>&filterTipoActa=<tipoActa>&Error<error>', methods=['POST', 'GET'])
# def get_allMCADbySecTipoActaError(sec,tipoActa,error):
#     conn = mysql.connect()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     cur.execute('SELECT FechaMCADterminal,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE Sec = %s AND TipoAct = %s AND Error = %s;' (sec,tipoActa))
#     rows = cur.fetchall()
#     resp = jsonify(rows)
#     resp.status_code=200
#     return resp

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
# @app.route('/ValuesTCA/filterError=<error>', methods=['POST', 'GET'])
# def get_allTCAbyError(error):
#     conn = mysql.connect()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE Error = %s ORDER BY RAND();',(error))
#     rows = cur.fetchall()
#     resp = jsonify(rows)
#     resp.status_code=200
#     return resp

#* This endpoint gets all the records of the TCA terminal by type of record and Sec.
@app.route('/ValuesTCA/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_aTCAbySecATipoAct(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;',(sec,tipoActa))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all history from TCA terminal by type of record and Sec.
@app.route('/HistoryTCA/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_historyTCAbySecATipoAct(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT IpTCA1, UsuarioTCA1, FechaTCA1, ErrorTCA1, IpTCA2, UsuarioTCA2, FechaTCA2, ErrorTCA2, IpTCA3, UsuarioTCA3, FechaTCA3, ErrorTCA3, IpTCA4, UsuarioTCA4, FechaTCA4, ErrorTCA4 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;',(sec,tipoActa))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

# #* This endpoint gets all the records of the TCA terminal by type of record, Sec and if the record has an error.
# @app.route('/ValuesTCA/filterSec=<sec>&filterTipoActa=<tipoActa>&filterError=<error>', methods=['POST', 'GET'])
# def get_RealTCAbySecATipoActAError(sec,tipoActa,error):
#     conn = mysql.connect()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s AND Error = %s;',(sec,tipoActa,error))
#     rows = cur.fetchall()
#     cur.close()
#     resp = jsonify(rows)
#     resp.status_code=200
#     return resp

#* This endpoint creates add a service record to some terminal of the TCA
@app.route('/addTCA', methods=['PUT'])
def update_tcaServiceActivityTerminalOne():
    if request.method == 'PUT':
        json_data = request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        ipTCA = json_data['IpTCA']
        fechaTCA = datetime.datetime.now()
        usuarioTCA = json_data['UsuarioTCA']
        errorTCA = json_data['ErrorTCA']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT UsuarioTCA1 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
        rows = cur.fetchone() # rows es un diccionario
        usuario = str(rows['UsuarioTCA1']) #Guardamos el valor 
        print(usuario)
        if usuario == 'None':
            cur.execute('UPDATE ServiceTable SET IpTCA1 = %s ,UsuarioTCA1 = %s,FechaTCA1 = %s , ErrorTCA1 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
            conn.commit()
            resp = jsonify(cur.rowcount)
            resp.status_code=200
        else:
            cur.execute('SELECT UsuarioTCA2 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
            rows = cur.fetchone() # rows es un diccionario
            usuario = str(rows['UsuarioTCA2']) #Guardamos el valor 
            if usuario == 'None':
                cur.execute('UPDATE ServiceTable SET IpTCA2= %s ,UsuarioTCA2 = %s , FechaTCA2 = %s, ErrorTCA2 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
                conn.commit()
                resp = jsonify(cur.rowcount)
                resp.status_code=200
            else:
                cur.execute('SELECT UsuarioTCA3 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
                rows = cur.fetchone() # rows es un diccionario
                usuario = str(rows['UsuarioTCA3']) #Guardamos el valor 
                if usuario == 'None':
                    cur.execute('UPDATE ServiceTable SET IpTCA3 = %s ,UsuarioTCA3 = %s , FechaTCA3 = %s, ErrorTCA3 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
                    conn.commit()
                    resp = jsonify(cur.rowcount)
                    resp.status_code=200
                else:
                    cur.execute('SELECT UsuarioTCA4 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
                    rows = cur.fetchone() # rows es un diccionario
                    usuario = str(rows['UsuarioTCA4']) #Guardamos el valor 
                    if usuario == 'None':
                        cur.execute('UPDATE ServiceTable SET IpTCA4 = %s ,UsuarioTCA4 = %s , FechaTCA4 =, ErrorTCA4 = %s %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
                        conn.commit()
                        resp = jsonify(cur.rowcount)
                        resp.status_code=200
                    else:
                        resp = jsonify(cur.rowcount)
                        resp.status_code=400
        return resp
    
#* This endpoint creates add a service record to terminal three of the COT
@app.route('/addCOT', methods=['PUT'])
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