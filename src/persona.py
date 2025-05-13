class Persona:
    
    def __init__(self, nombre, apellido, dni):
        

        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not apellido or not apellido.strip():
            raise ValueError("El apellido no puede estar vacío")
        if not dni or not dni.strip():
            raise ValueError("El DNI no puede estar vacío")
        if not dni.isdigit():
            raise ValueError("El DNI debe contener solo dígitos")
        
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<no penso en nada>"


    def __repr__(self):
        
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    #Mejoré el método pensar para que revise que el pesamiento se texto y que no sea una cadena vacía
    def pensar(self, idea):
        
        if idea is None:
            raise TypeError("La idea no puede ser None")
        
        if not isinstance(idea, str):
            raise TypeError("La idea debe ser una cadena de texto")
        
        if not idea.strip():
            raise ValueError("La idea no puede estar vacía")
        self.pensamientos += 1
        self.ultima_idea = idea