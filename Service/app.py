import time
import json
import pymysql
import datetime
from flask import Flask, request, flash, jsonify
from flaskext.mysql import MySQL

# FLASK Instance my application
app = Flask(__name__)
PORT = 5000
DEBUG = False
mysql = MySQL()

##
# Generating the configuration to the connection to the DB
# Change the values of each config according to your credentials from your local DB
##

app.config['MYSQL_DATABASE_USER'] = 'u917498081_servicedb'
app.config['MYSQL_DATABASE_PASSWORD'] = '$|OS8YaC/r5I'
app.config['MYSQL_DATABASE_DB'] = 'u917498081_INEDATABASE'
app.config['MYSQL_DATABASE_HOST'] = 'www.taquitosoftware.com.mx'


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
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE TipoActa = %s;', (tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint obtains the record by type of act and Sec
@app.route('/historyService/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['GET'])
def get_historyServiceBySecTipoActa(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE Sec = %s AND TipoActa = %s ;', (sec,tipoActa))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint obtains the record by shaMCAD
@app.route('/historyService/filterShaMCAD=<shaMCAD>', methods=['GET'])
def get_historyServiceByshaMCAD(shaMCAD):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE ShaMCAD = %s ;', (shaMCAD))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint obtains the record by shaTCA
@app.route('/historyService/filterShaTCA=<shaTCA>', methods=['GET'])
def get_historyServiceByshaTCA(shaTCA):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE ShaTCA = %s ;', (shaTCA))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint obtains the record by shaCotejo
@app.route('/historyService/filterShaCotejo=<shaCotejo>', methods=['GET'])
def get_historyServiceByshaCotejo(shaCotejo):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable WHERE ShaCotejo = %s ;', (shaCotejo))
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

#* This endpoint gets all the records of the Cotejo terminal by ShaCotejo.
@app.route('/terminalCotejo/filterShaCotejo=<ShaCotejo>', methods=['POST', 'GET'])
def get_allMCADbyShaCotejo(ShaCotejo):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT IpCotejo,UsuarioCotejo,FechaCotejo,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE ShaCotejo = %s;',  (shaCotejo))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the MCAD terminal by shaMCAD.
@app.route('/terminalMCAD/filterShaMCAD=<shaMCAD>', methods=['POST', 'GET'])
def get_allMCADbyShaMCAD(shaMCAD):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT IpMCAD,UsuarioMCAD,FechaMCAD,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE ShaMCAD = %s;',  (shaMCAD))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint add data to MCAD register
@app.route('/terminalMCAD/addShaMCAD', methods=['PUT'])
def update_cotServiceActivity():
    if request.method == 'PUT':
        flag = 1
        json_data = request.get_json()
        tipoQr = json_data['TipoQR']
        estado = json_data['Estado']
        distrito = json_data['Distrito']
        seccion = json_data['Seccion']
        casilla = json_data['Casilla']
        tipoActa = json_data['TipoActa']
        shaMCAD = json_data['ShaMCAD'] 
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET ShaMCAD = %s, Flag = %s WHERE TipoQR = %s, Estado = %s, Distrito = %s, Seccion = %s, Casilla = %s, TipoActa = %s ;', (shaMCAD,flag,tipoQr,estado,distrito,seccion,casilla,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
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
    cur.execute('SELECT BolSob,PersVot,TotPVnRep,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable ORDER BY RAND();')
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the TCA terminal by type of act and Sec.
@app.route('/ValuesTCA/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
def get_aTCAbySecATipoAct(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT BolSob,PersVot,TotPVnRep,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;',(sec,tipoActa))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all the records of the TCA terminal by shaTCA.
@app.route('/ValuesTCA/filterShaTCA=<shaTCA>', methods=['POST', 'GET'])
def get_aTCAbyShaTCA(shaTCA):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT BolSob,RepVot,PersVot,TotPVnRep,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable WHERE ShaTCA = %s;',(shaTCA))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all history from TCA terminal by shaMCAD.
@app.route('/HistoryTCA/filterShaMCAD=<shaMCAD>', methods=['POST', 'GET'])
def get_historyTCAbyShaMCAD(shaMCAD):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT IpTCA1, UsuarioTCA1, FechaTCA1, ErrorTCA1, IpTCA2, UsuarioTCA2, FechaTCA2, ErrorTCA2, IpTCA3, UsuarioTCA3, FechaTCA3, ErrorTCA3, IpTCA4, UsuarioTCA4, FechaTCA4, ErrorTCA4 FROM ServiceTable WHERE ShaMCAD = %s;',(shaMCAD))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint gets all history from TCA terminal by shaTCA.
@app.route('/HistoryTCA/filterShaTCA=<shaTCA>', methods=['POST', 'GET'])
def get_historyTCAbyShaTCA(shaTCA):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT IpTCA1, UsuarioTCA1, FechaTCA1, ErrorTCA1, IpTCA2, UsuarioTCA2, FechaTCA2, ErrorTCA2, IpTCA3, UsuarioTCA3, FechaTCA3, ErrorTCA3, IpTCA4, UsuarioTCA4, FechaTCA4, ErrorTCA4 FROM ServiceTable WHERE ShaTCA = %s ;',(shaTCA))
    rows = cur.fetchall()
    cur.close()
    resp = jsonify(rows)
    resp.status_code=200
    return resp


#* This endpoint creates/add a service record to some terminal of the TCA
@app.route('/addTCA', methods=['PUT'])
def update_tcaServiceActivityTerminalbyShaTCA():
    if request.method == 'PUT':
        json_data = request.get_json()
        shaTCA = json_data['ShaTCA']
        ipTCA = json_data['IpTCA']
        fechaTCA = datetime.datetime.now()
        usuarioTCA = json_data['UsuarioTCA']
        errorTCA = json_data['ErrorTCA']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT UsuarioTCA1 FROM ServiceTable WHERE ShaTCA = %s;', (shaTCA))
        rows = cur.fetchone() # rows es un diccionario
        usuario = str(rows['UsuarioTCA1']) #Guardamos el valor 
        print(usuario)
        if usuario == 'None':
            cur.execute('UPDATE ServiceTable SET IpTCA1 = %s ,UsuarioTCA1 = %s,FechaTCA1 = %s , ErrorTCA1 = %s WHERE ShaTCA = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,shaTCA))
            conn.commit()
            resp = jsonify(cur.rowcount)
            resp.status_code=200
        else:
            cur.execute('SELECT UsuarioTCA2 FROM ServiceTable WHERE ShaTCA = %s;', (shaTCA))
            rows = cur.fetchone() # rows es un diccionario
            usuario = str(rows['UsuarioTCA2']) #Guardamos el valor 
            if usuario == 'None':
                cur.execute('UPDATE ServiceTable SET IpTCA2= %s ,UsuarioTCA2 = %s , FechaTCA2 = %s, ErrorTCA2 = %s WHERE ShaTCA = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,shaTCA))
                conn.commit()
                resp = jsonify(cur.rowcount)
                resp.status_code=200
            else:
                cur.execute('SELECT UsuarioTCA3 FROM ServiceTable WHERE ShaTCA = %s;', (shaTCA))
                rows = cur.fetchone() # rows es un diccionario
                usuario = str(rows['UsuarioTCA3']) #Guardamos el valor 
                if usuario == 'None':
                    cur.execute('UPDATE ServiceTable SET IpTCA3 = %s ,UsuarioTCA3 = %s , FechaTCA3 = %s, ErrorTCA3 = %s WHERE ShaTCA = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,shaTCA))
                    conn.commit()
                    resp = jsonify(cur.rowcount)
                    resp.status_code=200
                else:
                    cur.execute('SELECT UsuarioTCA4 FROM ServiceTable WHERE ShaTCA = %s;', (shaTCA))
                    rows = cur.fetchone() # rows es un diccionario
                    usuario = str(rows['UsuarioTCA4']) #Guardamos el valor 
                    if usuario == 'None':
                        cur.execute('UPDATE ServiceTable SET IpTCA4 = %s ,UsuarioTCA4 = %s , FechaTCA4 = %s, ErrorTCA4 = %s WHERE ShaTCA = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,shaTCA))
                        conn.commit()
                        resp = jsonify(cur.rowcount)
                        resp.status_code=200
                    else:
                        resp = jsonify(cur.rowcount)
                        resp.status_code=400
        return resp
    

#* This endpoint creates/add a service record to terminal COT
@app.route('/addCOT', methods=['PUT'])
def update_cotServiceActivity():
    if request.method == 'PUT':
        json_data = request.get_json()
        shaCotejo = json_data['ShaCotejo']
        ipCotejo = json_data['IpCotejo']
        fechaCotejo = datetime.datetime.now()
        usuarioCotejo = json_data['UsuarioCotejo']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET IpCotejo = %s ,UsuarioCotejo = %s , FechaCotejo = %s WHERE ShaCotejo = %s;', (ipCotejo,usuarioCotejo,fechaCotejo,shaCotejo))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp

#* This endpoint creates/add a service record to terminal MCAD
@app.route('/addMCAD', methods=['PUT'])
def update_MCADnServiceActivity():
    if request.method == 'PUT':
        json_data = request.get_json()
        shaMCAD = json_data['ShaMCAD']
        ipMCAD = json_data['IpMCAD']
        fechaMCAD = datetime.datetime.now()
        usuarioMCAD = json_data['UsuarioMCAD']  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET IpMCAD = %s ,UsuarioMCAD = %s , FechaMCAD = %s WHERE ShaMCAD = %s;', (ipMCAD,usuarioMCAD,fechaMCAD,shaMCAD))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp

#* This endpoint deletes a complete register by sec and Act type
@app.route('/upsi/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['DELETE'])
def delete_actBy(sec,tipoActa):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM ServiceTable WHERE Sec = %s AND TipoAct = %s;',  (sec,tipoActa))
    conn.commit()
    rows = cur.fetchone() # rows es un diccionario
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#* This endpoint updates a register in TCA with its own sha code
@app.route('/updateShaTCA', methods=['PUT'])
def update_shaTCA():
    if request.method == 'PUT':
        json_data = request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        shaTCA = json_data['ShaTCA']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET ShaTCA = %s WHERE Sec = %s AND TipoActa = %s ;', (shaTCA,sec,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        resp.status_code=200
        return resp
    
#* This endpoint updates a register in MCAD with its own sha code
@app.route('/updateShaMCAD', methods=['PUT'])
def update_shaMCAD():
    if request.method == 'PUT':
        json_data = request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        shaMCAD = json_data['ShaMCAD'] 
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET ShaMCAD = %s WHERE Sec = %s AND TipoActa = %s ;', (shaMCAD,sec,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        resp.status_code=200
        return resp
     
#* This endpoint updates a register in Cotejo with its own sha code
@app.route('/updateShaCotejo', methods=['PUT'])
def update_shaCotejo():
    if request.method =='PUT':
        json_data =request.get_json()
        sec = json_data['Sec']
        tipoActa = json_data['TipoActa']
        shaCotejo = json_data['ShaCotejo']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE ServiceTable SET ShaCotejo = %s WHERE Sec = %s AND TipoActa = %s ;', (shaCotejo,sec,tipoActa))
        conn.commit()
        resp = jsonify(cur.rowcount)
        resp.status_code=200
        return resp
    
#* This endpoint gets Act type by shaMCAD
@app.route('/tipoActabyShaMCAD=<shaMCAD>', methods=['GET'])
def get_typeAct(shaMCAD):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT TipoActa FROM ServiceTable WHERE ShaMCAD = %s;',(shaMCAD))
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)