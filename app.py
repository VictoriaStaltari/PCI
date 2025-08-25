from flask import Flask, render_template, request, json
from clases import Carrera, Materia
from func import priorizar_materias, organizar, ajustar_cuatrimestres

app = Flask(__name__)

# Ruta principal: muestra la página inicial
# Redirige hacia la ruta de la carrera

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/carrera/<nombre_carrera>')
def plan_carrera(nombre_carrera):
    nombreJSON = f'planes/{nombre_carrera}.json'
    with open(nombreJSON, 'r', encoding='utf-8') as f:
        plan_carrera = json.load(f) # Carga el plan de carrera desde el archivo JSON

    materias = plan_carrera.get('materias_totales', []) #Pide la lista de materias segun el plan
    return render_template('carrera.html', carrera=nombre_carrera, materias=materias)


@app.route('/carrera/<nombre_carrera>/planificador', methods=['POST'])
def planificador(nombre_carrera):
    materias_aprobadas = request.form.getlist('materias_aprobadas')
    cant_materias = int(request.form['cant_materias'])
    cuatrimestre_actual = int(request.form['cuatrimestre_actual'])

    nombreJSON = f'planes/{nombre_carrera}.json'
    with open(nombreJSON, 'r', encoding="UTF-8") as f:
        plan_carrera = json.load(f)

    carrera = Carrera.from_dict(plan_carrera)
        
    materias_aprobadas_obj = [materia for materia in carrera.materias_totales if materia.codigo in materias_aprobadas]

    materias_falt_ordenadas_prioridad = priorizar_materias(
        carrera.materias_faltantes(materias_aprobadas_obj)
    )

    cuatrimestres_organizados = ajustar_cuatrimestres(
        materias_falt_ordenadas_prioridad,
        cant_materias,
        cuatrimestre_actual,
        materias_aprobadas_obj
    )
    print(cuatrimestres_organizados)
    
    nombres_materias= []
    for cuatri in cuatrimestres_organizados:
        lista_materias = []
        for materia in cuatri:
            lista_materias.append(materia.nombre)
        nombres_materias.append(lista_materias)

    return render_template(
        'planificador.html',
        carrera=nombre_carrera,
        materias_aprobadas=materias_aprobadas,
        cant_materias=cant_materias,
        cuatrimestre_actual=cuatrimestre_actual,
        plan=plan_carrera,
        cuatrimestres_organizados=nombres_materias
    )

if __name__ == '__main__':
    app.run(debug=True)
