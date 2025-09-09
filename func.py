def priorizar_materias(materias_faltantes):
    # Ordena las materias por aquellas que son correlativas de más materias, y como segundo criterio aquellas que solo se dan en un cuatrimestre

    return sorted(
        materias_faltantes,
        key=lambda m: (
            -len(m.correlatividades), # Primero las que son correlativas de más materias
            1 if m.cuatrimestre == 0 else 0,
            m.cuatrimestre
        )
    )

def organizar(nro_materias_cuatrimeste, materias_faltantes, cuatri_actual, materias_aprobadas):
    """Organiza un cuatrimestre segun el cuatrimestre actual y el nro de materias por cuatrimestre

    Args:
        nro_materias_cuatrimeste (int): Número máximo de materias a cursar por cuatrimestre.
        materias_faltantes (list): Lista de objetos Materia que representan las materias aún no cursadas.
        cuatri_actual (int): El cuatrimestre actual en el que se están organizando las materias.
        materias_aprobadas (list): Lista de códigos de materias que han sido aprobadas.

    Returns:
        tupla: Una tupla que contiene una lista (la lista representa un cuatrimestre), la lista actualizada de materias faltantes y la lista actualizada de materias aprobadas.
    """
    salida = []  # Lista de cuatrimestres con materias cursables
    i = 0
    lista_aux = []
    while (len(salida)<nro_materias_cuatrimeste) and (len(materias_faltantes)>0) and (i<len(materias_faltantes)):

        # Si la materia es cursable en el cuatrimestre actual y cumple con las correlativas
        if (materias_faltantes[i].es_cursable(cuatri_actual))and(materias_faltantes[i].control_correlativas(materias_aprobadas)):
            materia = materias_faltantes.pop(i)
            salida.append(materia)
            lista_aux.append(str(materia.codigo))
        else:
            i += 1
    for codigo in lista_aux:
        materias_aprobadas.append(codigo)
    return salida, materias_faltantes, materias_aprobadas

def ajustar_cuatrimestres(materias_faltantes, nro_materias_cuatrimeste, cuatri_actual, materias_aprobadas): 
    i = 0 
    cuatrimestres_organizados = [] #Lista de listas(cuatrimestres)
    
    while len(materias_faltantes) > 0: 
        cuatrimestre, materias_faltantes, materias_aprobadas = organizar(nro_materias_cuatrimeste, materias_faltantes, cuatri_actual,materias_aprobadas)  
        
        # 1 cuatrimestre y materias que faltan
        cuatrimestres_organizados.append(cuatrimestre)
        cuatri_actual = cuatri_actual*(-1)

    return cuatrimestres_organizados