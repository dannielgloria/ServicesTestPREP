# #* This endpoint gets all the records of the MCAD terminal by type of record and Sec.
# @app.route('/terminalMCAD/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
# def get_allMCADbySecTipoActa(sec,tipoActa):
#     conn = mysql.connect()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     cur.execute('SELECT IpMCAD,UsuarioMCAD,FechaMCAD,Consec,TipoQR,Estado,Distrito,Seccion,Casilla,TipoActa, BolSob, PersVot, TotPVnRep FROM ServiceTable WHERE Sec = %s AND TipoAct = %s;',  (sec,tipoActa))
#     rows = cur.fetchall()
#     resp = jsonify(rows)
#     resp.status_code=200
#     return resp


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


#* This endpoint gets all history from TCA terminal by type of record and Sec.
# @app.route('/HistoryTCA/filterSec=<sec>&filterTipoActa=<tipoActa>', methods=['POST', 'GET'])
# def get_historyTCAbySecATipoAct(sec,tipoActa):
#     conn = mysql.connect()
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     cur.execute('SELECT IpTCA1, UsuarioTCA1, FechaTCA1, ErrorTCA1, IpTCA2, UsuarioTCA2, FechaTCA2, ErrorTCA2, IpTCA3, UsuarioTCA3, FechaTCA3, ErrorTCA3, IpTCA4, UsuarioTCA4, FechaTCA4, ErrorTCA4 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;',(sec,tipoActa))
#     rows = cur.fetchall()
#     cur.close()
#     resp = jsonify(rows)
#     resp.status_code=200
#     return resp

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

# #* This endpoint creates add a service record to some terminal of the TCA
# @app.route('/addTCA', methods=['PUT'])
# def update_tcaServiceActivityTerminalOne():
#     if request.method == 'PUT':
#         json_data = request.get_json()
#         sec = json_data['Sec']
#         tipoActa = json_data['TipoActa']
#         ipTCA = json_data['IpTCA']
#         fechaTCA = datetime.datetime.now()
#         usuarioTCA = json_data['UsuarioTCA']
#         errorTCA = json_data['ErrorTCA']  
#         conn = mysql.connect()
#         cur = conn.cursor(pymysql.cursors.DictCursor)
#         cur.execute('SELECT UsuarioTCA1 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
#         rows = cur.fetchone() # rows es un diccionario
#         usuario = str(rows['UsuarioTCA1']) #Guardamos el valor 
#         print(usuario)
#         if usuario == 'None':
#             cur.execute('UPDATE ServiceTable SET IpTCA1 = %s ,UsuarioTCA1 = %s,FechaTCA1 = %s , ErrorTCA1 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
#             conn.commit()
#             resp = jsonify(cur.rowcount)
#             resp.status_code=200
#         else:
#             cur.execute('SELECT UsuarioTCA2 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
#             rows = cur.fetchone() # rows es un diccionario
#             usuario = str(rows['UsuarioTCA2']) #Guardamos el valor 
#             if usuario == 'None':
#                 cur.execute('UPDATE ServiceTable SET IpTCA2= %s ,UsuarioTCA2 = %s , FechaTCA2 = %s, ErrorTCA2 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
#                 conn.commit()
#                 resp = jsonify(cur.rowcount)
#                 resp.status_code=200
#             else:
#                 cur.execute('SELECT UsuarioTCA3 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
#                 rows = cur.fetchone() # rows es un diccionario
#                 usuario = str(rows['UsuarioTCA3']) #Guardamos el valor 
#                 if usuario == 'None':
#                     cur.execute('UPDATE ServiceTable SET IpTCA3 = %s ,UsuarioTCA3 = %s , FechaTCA3 = %s, ErrorTCA3 = %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
#                     conn.commit()
#                     resp = jsonify(cur.rowcount)
#                     resp.status_code=200
#                 else:
#                     cur.execute('SELECT UsuarioTCA4 FROM ServiceTable WHERE Sec = %s AND TipoActa = %s;', (sec,tipoActa))
#                     rows = cur.fetchone() # rows es un diccionario
#                     usuario = str(rows['UsuarioTCA4']) #Guardamos el valor 
#                     if usuario == 'None':
#                         cur.execute('UPDATE ServiceTable SET IpTCA4 = %s ,UsuarioTCA4 = %s , FechaTCA4 =, ErrorTCA4 = %s %s WHERE Sec = %s AND TipoActa = %s ;', (ipTCA,usuarioTCA,fechaTCA,errorTCA,sec,tipoActa))
#                         conn.commit()
#                         resp = jsonify(cur.rowcount)
#                         resp.status_code=200
#                     else:
#                         resp = jsonify(cur.rowcount)
#                         resp.status_code=400
#         return resp

#* This endpoint creates add a service record to terminal three of the COT
# @app.route('/addCOT', methods=['PUT'])
# def update_cotServiceActivity():
#     if request.method == 'PUT':
#         json_data = request.get_json()
#         sec = json_data['Sec']
#         tipoActa = json_data['TipoActa']
#         ipCotejo = json_data['IpCotejo']
#         fechaCotejo = datetime.datetime.now()
#         usuarioCotejo = json_data['UsuarioCotejo']  
#         conn = mysql.connect()
#         cur = conn.cursor(pymysql.cursors.DictCursor)
#         cur.execute('UPDATE ServiceTable SET IpCotejo = %s ,UsuarioCotejo = %s , FechaCotejo = %s WHERE Sec = %s AND TipoActa = %s ;', (ipCotejo,usuarioCotejo,fechaCotejo,sec,tipoActa))
#         conn.commit()
#         resp = jsonify(cur.rowcount)
#         print (resp)
#         resp.status_code=200
#         return resp