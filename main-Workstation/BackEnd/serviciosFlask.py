from flask import Flask, jsonify, render_template, request
from logueo import ejecucion


app = Flask(__name__, template_folder='C:\\Desarrollo\\Mis Proyectos\\WorkstationFedeOlivera\\main-Workstation\\FrontEnd\\HTML\\templateFiles', static_folder='C:\\Desarrollo\\Mis Proyectos\\WorkstationFedeOlivera\\main-Workstation\\FrontEnd\\HTML\\staticFiles' )


@app.route('/inicio')
def home():
    return render_template('index.html')

@app.route('/forgot_password')
def forgot_password():
     return render_template('recuperarContraseña.html')



@app.route('/login', methods=['POST'])
def login(mail, password):
    mail = request.form['mail']
    password = request.form['password']

    if ejecucion(mail, password):
        mensaje = 'ok'
    else:
        mensaje = 'error en verificacion usuario/contraseña'

    return jsonify({'mensaje': mensaje})


if __name__ == '__main__':
    app.run(debug=True)






