from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('intento.html')

@app.route('/pruebaConexion')
def ejemplo():
    mensaje = "ok"
    return jsonify({'mensaje': mensaje})

if __name__ == '__main__':
    app.run(debug=True)