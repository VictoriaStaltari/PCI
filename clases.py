import copy
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
            cuatrimestre=data['cuatrimestre'],
            correlatividades=data['correlatividades']
        )

    def control_correlativas(self, materias_cursadas):
        puede_hacerse = True
        for correlativa in self.correlativas:
            if str(correlativa) not in materias_cursadas:
                puede_hacerse = False
        return puede_hacerse
    
    def es_cursable(self, cuatrimestre_actual):
        return (self.cuatrimestre == cuatrimestre_actual)or(self.cuatrimestre == 0)or(self.cuatrimestre==2*cuatrimestre_actual)
    
    # Si el cuatrimestre actual es igual al que se da.
    # Si el cuatrimestre de la materia es 0 lo cual significa que se puede cursar en cualquier cuatrimestre.
    # Si el cuatrimestre de la materia es el doble del cuatrimestre actual, es decir si el cuatrimestre actual es 1, el primero y la materia es anual (cuatrimestre de la materia aparece como 2)
    
    
class Carrera:
    def __init__(self, nombre, codigo, materias_totales):
        self.nombre = nombre
        self.codigo = codigo
        self.materias_totales = materias_totales
    
    @classmethod
    def from_dict(cls, data):
        materias = [Materia.from_dict(m) for m in data['materias_totales']]
        return cls(
            nombre=data['nombre'],
            codigo=data['codigo'],
            materias_totales=materias
        )

    def agregar_materia(self, materia):
        if materia not in self.materias_totales:
            self.materias_totales.append(materia)

    def materias_faltantes(self, materias_cursadas):
        materias_faltantes = self.materias_totales
        lista_aux = []
        for codigo in materias_cursadas:
            codigo = int(codigo)
            for materia in materias_faltantes:
                if materia.codigo == codigo:
                    lista_aux.append(materia)
        materias_faltantes = [m for m in materias_faltantes if m not in lista_aux]
        return materias_faltantes