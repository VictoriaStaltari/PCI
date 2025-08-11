class Materia:
    def __init__(self, nombre, codigo, correlativas, correlatividades, cuatrimestre):
        self.nombre = nombre
        self.codigo = codigo
        self.correlativas = correlativas
        self.cuatrimestre = cuatrimestre
        self.correlatividades = correlatividades
        # Cuatrimestre 1(primero) -1(segundo) 0(ambos)

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data['nombre'],
            codigo=data['codigo'],
            correlativas=data['correlativas'],
            cuatrimestre=data['cuatrimestre']
        )

    def control_correlativas(self, materias_cursadas):
        puede_hacerse = True
        for correlativa in self.correlativas:
            if correlativa not in materias_cursadas:
                puede_hacerse = False
        return puede_hacerse
    
    def es_cursable(self, cuatrimestre_actual):
        return (self.cuatrimestre == cuatrimestre_actual)or(self.cuatrimestre == 0)
    
class Carrera:
    def __init__(self, nombre, codigo, materias_totales):
        self.nombre = nombre
        self.codigo = codigo
        self.materias_totales = materias_totales
    
    @classmethod
    def from_dict(cls, data):
        materias = [Materia.from_dict(m) for m in data['materiasTotales']]
        return cls(
            nombre=data['nombre'],
            codigo=data['codigo'],
            materias_totales=materias
        )

    def agregar_materia(self, materia):
        if materia not in self.materias_totales:
            self.materias_totales.append(materia)

    def materias_faltantes(self, materias_cursadas):
        return [materia for materia in self.materias_totales if materia not in materias_cursadas]


# No nos conviene usar clases 