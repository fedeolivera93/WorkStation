import sqlite3
miConexion = sqlite3.connect('base.db')
miCursor = miConexion.cursor()



def verificarMailSQL(mail, miCursor):
    miCursor.execute("SELECT * FROM mail") 
    listaEmail = miCursor.fetchall()
    for listaEmail in mail:
        if mail in listaEmail: 
            return True
    return False

def verificarPasswordSQL(password, miCursor):
    miCursor.execute("SELECT * FROM clave_acceso") 
    listaPassword = miCursor.fetchall()
    for listaPassword in password:
        if password in listaPassword: 
            return True
    return False

miConexion.close()




