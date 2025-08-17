def priorizar_materias(materias_faltantes):
    # Ordena las materias por aquellas que son correlativas de más materias, y como segundo criterio aquellas que solo se dan en un cuatrimestre

    return sorted(
        materias_faltantes,
        key=lambda m: (
            -len(m.correlatividades), 
            1 if m.cuatrimestre == 0 else 0, m.cuatrimestre
            )
    )

def organizar (nro_materias_cuatrimeste,materias_faltantes):  #recibe jnuemro de materias por cuatrimestre y materias faltantes y devuelve una lista de listas separadas 
    salida = [[]]  # empezamos con la primera lista         # en cuatrimestres con las materias que se pueden cursar y la lista actualizada de materias flatantes 
    i = 0
    eliminar_sin_irse_de_rango= []
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
    
    










        
