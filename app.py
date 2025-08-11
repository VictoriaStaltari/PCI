from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal: muestra la página inicial
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carrera/<nombre_carrera>')
def plan_carrera(nombre_carrera):
    return render_template('carrera.html', carrera=nombre_carrera)

# Ruta que se activa al hacer clic en el botón
@app.route('/carrera/<nombre_carrera>', methods=['POST'])
def procesar(nombre_carrera):
    dato = request.form['']
    
@app.route('/carrera/<nombre_carrera>/planificador')
def planificador(nombre_carrera):
    materias_cursadas = request.form.getlist('materiasCursadas')
    materias_por_cuatrimestre = int(request.form['materiasPorCuatrimestre'])
    
    # Aquí se procesaría la lógica para planificar las materias
    # Por ejemplo, se podría llamar a una función que use las clases Carrera y Materia
    
    cuatrimestres_organizados = []
    return render_template('planificador.html', cuatrimestres_organizados=cuatrimestres_organizados)

if __name__ == '__main__':
    app.run(debug=True)
