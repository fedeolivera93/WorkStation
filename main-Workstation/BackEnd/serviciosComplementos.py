import sqlite3
mi_conexion = sqlite3.connect('base.db')



def verificar(mail, micursor):
    micursor.execute("SELECT * FROM mail") 
    mail = micursor.fetchall()
    for user in mail:
        if mail in user: 
            return True
    return False

mi_conexion.close()




