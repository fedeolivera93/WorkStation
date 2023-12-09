import sqlite3, bcrypt

def verificarCredenciales (mailStr, passwordStr):
    miConexion = sqlite3.connect('base.db')
    miCursor = miConexion.cursor()



    # Busca el usuario por correo electrónico
    miCursor.execute("SELECT * FROM usuarios WHERE mail = ?", (mailStr,))
    usuario = miCursor.fetchone()

    # Verifica si el usuario existe y la contraseña coincide
    if usuario is not None and bcrypt.checkpw(passwordStr, usuario[2]):
        return True
    else:
        return False

    miConexion.close()




