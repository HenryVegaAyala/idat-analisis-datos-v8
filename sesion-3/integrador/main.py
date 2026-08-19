import numpy as np


class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = np.array(notas)

    def evaluar(self):
        promedio = np.mean(self.notas)

        if promedio >= 11:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        return f"{self.nombre}: {estado} ({promedio:.1f})"


alumno = Estudiante("María", [15, 14, 13, 11])
print(alumno.evaluar())
