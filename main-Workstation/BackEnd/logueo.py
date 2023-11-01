import re
import pyodbc

 
     

def validacionMailSintaxis(correo,clave):

    
    # verifica que el correo tenga el formato correcto
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", correo):
        return False

    
    # verifica que el correo contenga una de las direcciones de correo electrónico permitidas
    dominios_permitidos = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    for dominio in dominios_permitidos:
        if dominio in correo:
            return True
    return False



def claveAccesoParametro(correo, clave):
    # verifica que la contraseña tenga al menos una letra mayúscula
    if not re.search(r"[A-Z]", clave):
        return False

    # verifica que la contraseña tenga al menos una letra minúscula
    if not re.search(r"[a-z]", clave):
        return False

    # verifica que la contraseña tenga al menos un número
    if not re.search(r"[0-9]", clave):
        return False

    # verifica que la contraseña tenga al menos un carácter especial
    caracteres_especiales = [",", ".", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "<", ">", "?", "/"]
    if not re.search(r"[{}]".format("|".join(caracteres_especiales)), clave):
        return False

    return True


def comprobarSQL(correo, clave):


  # Configura tus propios parámetros de conexión
    server = 'DESKTOP-EU4H1J4' 
    database = 'workstation' 
    username = correo 
    password = clave 

    # Crea la cadena de conexión
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=' + server + ';'
        r'DATABASE=' + database + ';'
        r'UID=' + username + ';'
        r'PWD=' + password + ';'
    )

    # Establece la conexión
    conn = pyodbc.connect(conn_str)
    print(conn)
    if conn != False:
       print("conectado")

    # Crea un cursor
    cursor = conn.cursor()

    return cursor




def ejecucion():
 intentos = 0
 while intentos<3:
     
      correo = input("Mail")
      clave = input("Contraseña")
      validacionMailSintaxis(correo, clave)
      claveAccesoParametro(clave,correo)
      if validacionMailSintaxis(correo, clave) and claveAccesoParametro(correo, clave):
       comprobarSQL(correo, clave)
      else:
       intentos += 1
       if intentos<3:
        repetir = input("¿Reintentar? (S/N): ")
        if repetir.lower() != "s":
         break
    
 if intentos == 3:
   print("imposible, intentos agotados. Afuera maestro")   

ejecucion()


