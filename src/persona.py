class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<no penso en nada>"


    def __repr__(self):
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    #Mejoré el método pensar para que revise que el pesamiento se texto y que no sea una cadena vacía
    def pensar(self, idea):
        if not isinstance(idea, str):
            raise TypeError("La idea debe ser una cadena de texto")
        
        if not idea.strip():
            raise ValueError("La idea no puede estar vacía")
        self.pensamientos += 1
        self.ultima_idea = idea
    