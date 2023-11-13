from flask import Flask, jsonify, render_template


app = Flask(__name__, template_folder='C:\\Desarrollo\\Workstation\\main-Workstation\\FrontEnd\\HTML')

@app.route('/inicio')
def home():
    return render_template('index.html')

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
