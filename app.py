from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal: muestra la página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Ruta que se activa al hacer clic en el botón
@app.route('/procesar', methods=['POST'])
def procesar():
    dato = request.form['nombre']
    return f"<h2>Hola, {dato}. Procesamos tu input.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
