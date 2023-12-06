import re
import connectionSQL
 
     

def validacionMailSintaxis(mailStr):

    # verifica que el correo tenga el formato correcto
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", mailStr):
        return False


    
    # verifica que el correo contenga una de las direcciones de correo electrónico permitidas
    dominios_permitidos = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    for dominio in dominios_permitidos:
        if dominio in mailStr:
            return True
    return False



def claveAccesoParametro(passwordStr):
    # verifica que la contraseña tenga al menos una letra mayúscula
    if not re.search(r"[A-Z]", passwordStr):
        return False

    # verifica que la contraseña tenga al menos una letra minúscula
    if not re.search(r"[a-z]", passwordStr):
        return False

    # verifica que la contraseña tenga al menos un número
   # if not re.search(r"[0-9]", passwordStr):
    #    return False

    # verifica que la contraseña tenga al menos un carácter especial
    caracteres_especiales = [",", ".", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "<", ">", "?", "/"]
    if not re.search(r"[{}]".format("|".join(caracteres_especiales)), passwordStr):
        return False

    return True


def ejecucion(mail, password):
    
        mailStr = str(mail)
        passwordStr = str(password)
      
 
        validacionMailSintaxis(mailStr)
        claveAccesoParametro(passwordStr)
        if validacionMailSintaxis(mailStr, passwordStr) and claveAccesoParametro(mailStr, passwordStr) == True:
            connectionSQL.verificarMailSQL(mailStr) and connectionSQL.verificarPasswordSQL(passwordStr) == True
            return True
        else:
          return False
       


