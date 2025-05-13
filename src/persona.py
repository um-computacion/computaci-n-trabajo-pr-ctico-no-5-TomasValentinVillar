class Persona:
    """Clase que representa a una persona.
    
    Esta clase sirve como base para el sistema y contiene atributos y métodos 
    comunes para todas las personas.
    
    Attributes:
        nombre (str): Nombre de la persona.
        apellido (str): Apellido de la persona.
        dni (str): Documento de identidad de la persona (solo dígitos).
        pensamientos (int): Contador de pensamientos registrados.
        ultima_idea (str): El último pensamiento registrado.
    """
    def __init__(self, nombre, apellido, dni):
        """Inicializa una nueva instancia de la clase Persona.
        
        Args:
            nombre (str): Nombre de la persona.
            apellido (str): Apellido de la persona.
            dni (str): Documento de identidad de la persona.
            
        Raises:
            ValueError: Si alguno de los campos está vacío o si el DNI no tiene formato válido.
        """

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
        """Retorna una representación del objeto Persona.
        
        Returns:
            str: Representación de la persona.
        """
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    #Mejoré el método pensar para que revise que el pesamiento se texto y que no sea una cadena vacía
    def pensar(self, idea):
        """Registra un nuevo pensamiento de la persona y actualiza su última idea.
        
        Args:
            idea (str): El nuevo pensamiento o idea de la persona.
        
        Raises:
            TypeError: Si la idea no es una cadena de texto o es None.
            ValueError: Si la idea es una cadena vacía.
        """
        if idea is None:
            raise TypeError("La idea no puede ser None")
        
        if not isinstance(idea, str):
            raise TypeError("La idea debe ser una cadena de texto")
        
        if not idea.strip():
            raise ValueError("La idea no puede estar vacía")
        self.pensamientos += 1
        self.ultima_idea = idea