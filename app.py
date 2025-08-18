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
    return render_template('carrera.html', carrera=nombre_carrera)

@app.route('/carrera/<nombre_carrera>/planificador')
def planificador(nombre_carrera):
    materias_cursadas = request.form.getlist('materiasCursadas')
    materias_por_cuatrimestre = int(request.form['materiasPorCuatrimestre'])
    
    # Aquí se procesaría la lógica para planificar las materias
    # Por ejemplo, se podría llamar a una función que use las clases Carrera y Materia
   
    def ajustar_cuatriimestres(nro_materias_cuatrimeste, materias_faltantes): 
    i = 0 
    salida_final = [[]]

    while len(materias_faltantes) > 0: 
        salida, materias_faltantes = organizar(nro_materias_cuatrimeste, materias_faltantes)  # salida es lista de listas
        
        for cuatri in salida:  # 'cuatri' es una lista de materias
            if i >= len(salida_final):  # Si no existe la sublista, la agregamos
                salida_final.append([])
            
            # Intentamos agregar materias a la sublista actual
            while cuatri:  # mientras queden materias en esta lista de cuatrimestre
                espacio = nro_materias_cuatrimeste - len(salida_final[i])
                if espacio > 0:
                    # Agregamos hasta llenar el cuatrimestre actual
                    salida_final[i].extend(cuatri[:espacio])
                    cuatri = cuatri[espacio:]  # removemos las materias agregadas
                if len(salida_final[i]) >= nro_materias_cuatrimeste:
                    i += 1  # pasamos al siguiente cuatrimestre

    return salida_final
    
    # 1) Traer el plan
    # 2) Convertirlo a diccionario y dsp a clases
    # 3) la lista de materias aprobadas
    # 4) materias faltantes, lista
    # 5) ordenar la lista
    # 6) armar los cuatrimestres
    
    cuatrimestres_organizados = []
    return render_template('planificador.html', cuatrimestres_organizados=cuatrimestres_organizados)

if __name__ == '__main__':
    app.run(debug=True)
