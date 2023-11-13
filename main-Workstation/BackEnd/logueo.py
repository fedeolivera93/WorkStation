import re
import connectionSQL
 
     

def validacionMailSintaxis(mail):

    # verifica que el correo tenga el formato correcto
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", mail):
        return False

    
    # verifica que el correo contenga una de las direcciones de correo electrónico permitidas
    dominios_permitidos = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    for dominio in dominios_permitidos:
        if dominio in mail:
            return True
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
    if not re.search(r"[{}]".format("|".join(caracteres_especiales)), clave):
        return False

    return True


def ejecucion(mail, password):
 
      validacionMailSintaxis(mail, password)
      claveAccesoParametro(password,mail)
      if validacionMailSintaxis(mail, password) and claveAccesoParametro(mail, password) == True:
        connectionSQL
      else:
          return False
       
       

ejecucion()


