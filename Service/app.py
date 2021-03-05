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

# app.secret_key = "nsiSQPCXioI0DRBky"

@app.route('/historyService', methods=['GET'])
def get_historyService():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM ServiceTable ORDER BY RAND();')
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp


@app.route('/terminalMCAD', methods=['POST', 'GET'])
def get_allMCAD():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT FechaMCADterminal,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable ORDER BY RAND();')
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

@app.route('/realValuesTCA', methods=['POST', 'GET'])
def get_allRealMCAD():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,C1,C2,C3,C4,CNoReg,VotNulos,Tot1,Tot2 FROM ServiceTable ORDER BY RAND();')
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code=200
    return resp

#  ** VERSION PARA PROTRACTOR **
# @app.route('/history', methods=['POST'])
# def add_paymentInfo():
#     if request.method == 'POST':
#         userName = request.get_json['userName']
#         pwd = request.get_json['pdw']
#         conn = database.connect()
#         cur = conn.cursor(pymysql.cursors.DictCursor)
#         cur.execute('SELECT userID FROM user WHERE userName = %s AND pwd= %s',(userName, pwd))
#         rows = cur.fetchall()
#         cur.close()
#         userId = rows[0]
#         dateService = datetime.datetime.now()
#         ipAddres = request.get_json['ipAddres']
            # conn = mysql.connect()
            # cur = conn.cursor(pymysql.cursors.DictCursor)
#         cur.execute('INSERT INTO activityHis (dateService,ipAddres,userId) VALUES (%s,%s,%s)', (dateService,ipAddres,userId))
#         conn.commit()
#         resp = jsonify(cur.rowcount)
#         resp.status_code=200
#         return resp

@app.route('/addActivity', methods=['POST'])
def update_serviceActivity():
    if request.method == 'POST':
        json_data = request.get_json()
        userId = json_data['userId']
        ipAddres = json_data['ipAddres']
        dateService = datetime.datetime.now()
        print (dateService)  
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('UPDATE INTO activityHis (dateService,ipAddres,userId) VALUES (%s,%s,%s)', (dateService,ipAddres,userId))
        conn.commit()
        resp = jsonify(cur.rowcount)
        print (resp)
        resp.status_code=200
        return resp
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=3000, debug=True)