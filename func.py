def priorizar_materias(materias_faltantes):
    # Ordena las materias por aquellas que son correlativas de más materias, y como segundo criterio aquellas que solo se dan en un cuatrimestre

    return sorted(
        materias_faltantes,
        key=lambda m: (
            -len(m.correlatividades), 
            1 if m.cuatrimestre == 0 else 0, m.cuatrimestre
            )
    )
    



def organizar(nro_materias_cuatrimeste, materias_faltantes):
    """Organiza las materias faltantes en cuatrimestres de acuerdo al número de materias por cuatrimestre.

    Args:
        nro_materias_cuatrimeste (int): Número máximo de materias a cursar por cuatrimestre.
        materias_faltantes (list): Lista de objetos Materia que representan las materias aún no cursadas.

    Returns:
        tuple: Una tupla que contiene una lista de listas (cada sublista representa un cuatrimestre con materias cursables) y la lista actualizada de materias faltantes.
    """
    salida = [[]]  # Lista de cuatrimestres con materias cursables
    i = 0
    eliminar_sin_irse_de_rango = []
    for materia in materias_faltantes:
        if materia.cursable():
            eliminar_sin_irse_de_rango.append(materia)
            if len(salida[i]) < nro_materias_cuatrimeste:
                salida[i].append(materia)
            else:
                i += 1
                salida.append([materia])
    for e in eliminar_sin_irse_de_rango:
        materias_faltantes.pop(materias_faltantes.index(e))

    return salida, materias_faltantes

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