import sqlite3
miConexion = sqlite3.connect('base.db')
miCursor = miConexion.cursor()



def verificarMailSQL(mailStr):
    miCursor.execute("SELECT * FROM mail") 
    listaEmail = miCursor.fetchall()
    for listaEmail in mailStr:
        if mailStr in listaEmail: 
            return True
    return False

def verificarPasswordSQL(passwordStr):
    miCursor.execute("SELECT * FROM clave_acceso") 
    listaPassword = miCursor.fetchall()
    for listaPassword in passwordStr:
        if passwordStr in listaPassword: 
            return True
    return False

miConexion.close()




