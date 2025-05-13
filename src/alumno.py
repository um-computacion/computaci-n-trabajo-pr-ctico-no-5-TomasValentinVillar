from src.persona import Persona

class Alumno(Persona):
    """Clase que representa a un Alumno, heredando de Persona.
    
    Añade atributos y comportamientos específicos de un alumno.
    
    Attributes:
        nombre (str): Nombre del alumno.
        apellido (str): Apellido del alumno.
        dni (str): Documento de identidad del alumno.
        legajo (str): Número de legajo o matrícula del alumno (debe comenzar con una letra).
    """
    def __init__(self, nombre, apellido, dni, legajo):
        """Inicializa una nueva instancia de la clase Alumno.
        
        Args:
            nombre (str): Nombre del alumno.
            apellido (str): Apellido del alumno.
            dni (str): Documento de identidad del alumno.
            legajo (str): Número de legajo o matrícula del alumno.
            
        Raises:
            ValueError: Si el legajo está vacío o no tiene el formato adecuado.
        """
        super().__init__(nombre, apellido, dni)
        if not legajo or not legajo.strip():
            raise ValueError("El legajo no puede estar vacío")
        if not legajo[0].isalpha():
            raise ValueError("El legajo debe comenzar con una letra")
        self.legajo = legajo

    def __repr__(self):
        """Retorna una representación del objeto Alumno.
        
        Returns:
            str: Representación SSdel alumno.
        """
    
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"