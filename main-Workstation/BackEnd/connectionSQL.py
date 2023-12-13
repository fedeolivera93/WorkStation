import sqlite3, bcrypt

def verificarCredenciales(mailStr, passwordStr):

    connection = sqlite3.connect('C:/Desarrollo/Workstation/main-Workstation/BackEnd/base.db')
    cursor = connection.cursor()

    mail_param = (mailStr,)
    password_param = passwordStr.encode('utf-8')  # Codifica la contraseña antes del uso

    try:
        cursor.execute("SELECT clave_acceso FROM usuarios WHERE mail = ?", mail_param)
        hashed_password = cursor.fetchone()

        if hashed_password and bcrypt.checkpw(password_param, hashed_password[0]):
            return True
        else:
            return False

    finally:
        cursor.close()
        connection.close()

