import sqlite3, bcrypt

def verificarCredenciales(mailStr, password):

    connection = sqlite3.connect('C:/Desarrollo/Mis Proyectos/WorkstationFedeOlivera/main-Workstation/BackEnd/base.db')
    cursor = connection.cursor()

    mail_param = (mailStr,)

    try:
        cursor.execute("SELECT clave_acceso FROM usuarios WHERE mail = ?", mail_param)
        resultado = cursor.fetchone()

        if password ==  resultado[0]:
         return True
        
    except sqlite3.Error as e:
        print(f"error: {e}")
    finally:
      cursor.close()

