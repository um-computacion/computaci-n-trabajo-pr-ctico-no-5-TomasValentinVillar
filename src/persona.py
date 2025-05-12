class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<no penso en nada>"

    #Implementé correctamente el método __str__ para satisfacer la 
    #prueba test_repr_persona que está verificando la salida de str(persona).

    def __str__(self):
        
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"

    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', apellido='{self.apellido}', dni='{self.dni}')"