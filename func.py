def priorizar_materias(materias_faltantes):
    # Ordena las materias por aquellas que son correlativas de más materias, y como segundo criterio aquellas que solo se dan en un cuatrimestre

    return sorted(
        materias_faltantes,
        key=lambda m: (
            -len(m.correlatividades), 
            1 if m.cuatrimestre == 0 else 0,
            m.cuatrimestre
            )
    )
    

def organizar(nro_materias_cuatrimeste, materias_faltantes, cuatri_actual):
    """Organiza un cuatrimestre segun el cuatrimestre actual y el nro de materias por cuatrimestre

    Args:
        nro_materias_cuatrimeste (int): Número máximo de materias a cursar por cuatrimestre.
        materias_faltantes (list): Lista de objetos Materia que representan las materias aún no cursadas.
        cuatri_actual (int): El cuatrimestre actual en el que se están organizando las materias.

    Returns:
        tupla: Una tupla que contiene una lista (la lista representa un cuatrimestre) y la lista actualizada de materias faltantes.
    """
    salida = []  # Lista de cuatrimestres con materias cursables
    i = 0
    while len(salida)<nro_materias_cuatrimeste and len(materias_faltantes)>0 and i<len(materias_faltantes):
        if materias_faltantes[i].es_cursable(cuatri_actual):
            materia = materias_faltantes.pop(i)
            salida.append(materia)
        else:
            i += 1
    return salida, materias_faltantes

def ajustar_cuatrimestres(materias_faltantes, nro_materias_cuatrimeste, cuatri_actual): 
    i = 0 
    cuatrimestres_organizados = [] #Lista de listas(cuatrimestres)

    while len(materias_faltantes) > 0: 
        cuatrimestre, materias_faltantes = organizar(nro_materias_cuatrimeste, materias_faltantes, cuatri_actual)  
        # 1 cuatrimestre y materias que faltan
        cuatrimestres_organizados.append(cuatrimestre)
        cuatri_actual = cuatri_actual*(-1)

    return cuatrimestres_organizados