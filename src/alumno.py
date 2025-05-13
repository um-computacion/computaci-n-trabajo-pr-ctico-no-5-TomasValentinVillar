from src.persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        if not legajo or not legajo.strip():
            raise ValueError("El legajo no puede estar vacío")
        if not legajo[0].isalpha():
            raise ValueError("El legajo debe comenzar con una letra")
        self.legajo = legajo

    def __repr__(self):
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"