import sqlite3, bcrypt

def verificarCredenciales(mailStr, passwordStr):


  connection = sqlite3.connect('base.db')
  cursor = connection.cursor()

  # Use parameter binding for mailStr
  mail_param = (mailStr,)

  try:
    # Use parameter placeholder in the query
    cursor.execute("SELECT * FROM usuarios WHERE mail = ?", mail_param)
    usuario = cursor.fetchone()

    # Check for user existence and password validity
    if usuario is not None and bcrypt.checkpw(passwordStr, usuario[2]):
      return True
    else:
      return False
  finally:
    # Close connection and cursor
    cursor.close()
    connection.close()
