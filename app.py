from flask import Flask, render_template, request, json
from clases import Carrera, Materia
from func import priorizar_materias, organizar

app = Flask(__name__)

# Ruta principal: muestra la página inicial
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/carrera/<nombre_carrera>')
def plan_carrera(nombre_carrera):
    nombreJSON = f'planes/{nombre_carrera}.json'
    with open(nombreJSON, 'r') as f:
        plan_carrera = json.load(f)

    materias = plan_carrera.get('materias_totales', [])
    return render_template('carrera.html', carrera=nombre_carrera, materias=materias)


@app.route('/carrera/<nombre_carrera>/planificador', methods=['POST'])
def planificador(nombre_carrera):
    materias_aprobadas = request.form.getlist('materias_aprobadas')
    cant_materias = int(request.form['cant_materias'])
    cuatrimestre_actual = int(request.form['cuatrimestre_actual'])

    nombreJSON = f'planes/{nombre_carrera}.json'
    with open(nombreJSON, 'r') as f:
        plan_carrera = json.load(f)

    # Aquí se procesaría la lógica para planificar las materias.
    # Se utilizarán las materias aprobadas, la cantidad de materias por cuatrimestre
    # y el plan de estudio obtenido del archivo JSON.
    cuatrimestres_organizados = []

    return render_template(
        'planificador.html',
        carrera=nombre_carrera,
        materias_aprobadas=materias_aprobadas,
        cant_materias=cant_materias,
        cuatrimestre_actual=cuatrimestre_actual,
        plan=plan_carrera,
        cuatrimestres_organizados=cuatrimestres_organizados,
    )

if __name__ == '__main__':
    app.run(debug=True)
