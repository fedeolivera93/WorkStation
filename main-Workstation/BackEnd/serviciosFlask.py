from flask import Flask, jsonify, render_template, url_for


app = Flask(__name__, template_folder='C:\\Desarrollo\\Mis Proyectos\\WorkstationFedeOlivera\\main-Workstation\\FrontEnd\\HTML\\templateFiles', static_folder='C:\\Desarrollo\\Mis Proyectos\\WorkstationFedeOlivera\\main-Workstation\\FrontEnd\\HTML\\staticFiles' )



@app.route('/inicio')
def home():
    return render_template('index.html')

@app.route('/forgot_password')
def forgot_password():
     return render_template('recuperarContraseña.html')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)




import logueo
import requests

@app.route('/login', methods=['POST'])
def login(mail, password):
    mail = requests.form['mail']
    password = requests.form['password']

    if logueo(mail, password) ==  True:
        mensaje = 'ok'
    else:
        mensaje = 'error'

    return jsonify({'mensaje': mensaje})

if __name__ == '__main__':
    app.run(debug=True)



