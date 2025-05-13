from src.persona import Persona

class Profesor(Persona):
    """Clase que representa a un Profesor, heredando de Persona.
    
    Añade atributos y comportamientos específicos de un profesor.
    
    Attributes:
        nombre (str): Nombre del profesor.
        apellido (str): Apellido del profesor.
        dni (str): Documento de identidad del profesor.
        sueldo (float): Sueldo del profesor (debe ser un valor positivo).
    """
    def __init__(self, nombre, apellido, dni, sueldo):
        """Inicializa una nueva instancia de la clase Profesor.
        
        Args:
            nombre (str): Nombre del profesor.
            apellido (str): Apellido del profesor.
            dni (str): Documento de identidad del profesor.
            sueldo (float): Sueldo del profesor.
            
        Raises:
            ValueError: Si el sueldo es cero o negativo.
            TypeError: Si el sueldo no es un valor numérico.
        """
        super().__init__(nombre, apellido, dni)
        if not isinstance(sueldo, (int, float)):
            raise TypeError("El sueldo debe ser un valor numérico")
        if sueldo <= 0:
            raise ValueError("El sueldo debe ser mayor que cero")
        self.sueldo = sueldo

    def __repr__(self):
        """Retorna una representación del objeto Profesor.
        
        Returns:
            str: Representación del profesor.
        """
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"