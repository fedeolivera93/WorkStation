import re
import connectionSQL
 
     

def validacionMailSintaxis(mail):


    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail) is not None

    
    # verifica que el correo contenga una de las direcciones de correo electrónico permitidas
    dominios_permitidos = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    dominio_actual = dominios_permitidos.pop(0)
    while dominio_actual:
        if dominio_actual in mail:
            return True
        dominio_actual = dominios_permitidos.pop(0)
    return False



def claveAccesoParametro(password):
    # verifica que la contraseña tenga al menos una letra mayúscula
    if not re.search(r"[A-Z]", password):
        return False

    # verifica que la contraseña tenga al menos una letra minúscula
    if not re.search(r"[a-z]", password):
        return False

    # verifica que la contraseña tenga al menos un número
    if not re.search(r"[0-9]", password):
        return False

    # verifica que la contraseña tenga al menos un carácter especial
    caracteres_especiales = [",", ".", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "<", ">", "?", "/"]
    if not re.search(r"[{}]".format("|".join(caracteres_especiales)), password):
        return False

    return True


def ejecucion(mail, password):
 
      validacionMailSintaxis(mail)
      claveAccesoParametro(password)
      if validacionMailSintaxis(mail, password) and claveAccesoParametro(mail, password) == True:
        if connectionSQL.verificarMailSQL(mail) and connectionSQL.verificarPasswordSQL(password) == True:
         return True
      else:
          return False
       


