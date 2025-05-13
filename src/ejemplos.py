"""
Ejemplos de uso del módulo de Personas, Alumnos y Profesores

Este script contiene ejemplos prácticos que demuestran cómo utilizar
las clases Persona, Alumno y Profesor, ilustrando los conceptos de
herencia, polimorfismo y encapsulamiento.
"""

from src.persona import Persona
from src.alumno import Alumno
from src.profesor import Profesor

def demostrar_creacion_basica():
    """Demuestra la creación básica de cada tipo de objeto."""
    print("\n1. CREACIÓN BÁSICA DE OBJETOS")
    print("=" * 50)
    
    # Crear una persona
    persona = Persona("Ana", "López", "87654321")
    print(f"Persona creada: {persona}")
    
    # Crear un alumno
    alumno = Alumno("Juan", "Pérez", "12345678", "A123")
    print(f"Alumno creado: {alumno}")
    
    # Crear un profesor
    profesor = Profesor("María", "García", "11223344", 50000)
    print(f"Profesor creado: {profesor}")

def demostrar_metodo_pensar():
    """Demuestra el uso del método pensar en cada clase."""
    print("\n2. USO DEL MÉTODO PENSAR")
    print("=" * 50)
    
    # Crear objetos
    persona = Persona("Ana", "López", "87654321")
    alumno = Alumno("Juan", "Pérez", "12345678", "A123")
    profesor = Profesor("María", "García", "11223344", 50000)
    
    # Hacer que cada uno piense algo
    persona.pensar("Me pregunto qué haré hoy")
    print(f"Persona pensó: {persona.ultima_idea}")
    print(f"Contador de pensamientos: {persona.pensamientos}")
    
    alumno.pensar("Tengo que estudiar para el examen")
    print(f"Alumno pensó: {alumno.ultima_idea}")
    print(f"Contador de pensamientos: {alumno.pensamientos}")
    
    profesor.pensar("Debo preparar la próxima clase")
    print(f"Profesor pensó: {profesor.ultima_idea}")
    print(f"Contador de pensamientos: {profesor.pensamientos}")

def demostrar_polimorfismo():
    """Demuestra el polimorfismo con una colección de objetos."""
    print("\n3. DEMOSTRACIÓN DE POLIMORFISMO")
    print("=" * 50)
    
    # Crear una colección de objetos de diferentes clases
    personas = [
        Persona("Ana", "López", "87654321"),
        Alumno("Juan", "Pérez", "12345678", "A123"),
        Profesor("María", "García", "11223344", 50000)
    ]
    
    # Iterar a través de la colección y hacer que cada objeto piense
    print("Haciendo que cada objeto piense:")
    for i, p in enumerate(personas, 1):
        p.pensar(f"Pensamiento número {i}")
        # El polimorfismo nos permite tratar a todos como personas
        # pero cada uno tendrá su propia representación en string
        print(f"{type(p).__name__}: {p}")

def demostrar_manejo_errores():
    """Demuestra cómo se manejan los errores y validaciones."""
    print("\n4. MANEJO DE ERRORES Y VALIDACIONES")
    print("=" * 50)
    
    print("Intentando crear objetos con valores inválidos:")
    
    try:
        # Intentar crear una persona con DNI no numérico
        Persona("Ana", "López", "ABC123")
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    try:
        # Intentar crear un alumno con legajo que no comienza con letra
        Alumno("Juan", "Pérez", "12345678", "123")
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    try:
        # Intentar crear un profesor con sueldo negativo
        Profesor("María", "García", "11223344", -5000)
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    try:
        # Intentar hacer que una persona piense algo que no es string
        persona = Persona("Ana", "López", "87654321")
        persona.pensar(123)
    except TypeError as e:
        print(f"Error esperado: {e}")
    
if __name__ == "__main__":
    print("EJEMPLOS DE USO DEL MÓDULO DE PERSONAS")
    print("=" * 50)
    
    demostrar_creacion_basica()
    demostrar_metodo_pensar()
    demostrar_polimorfismo()
    demostrar_manejo_errores()
    
    print("\nFin de los ejemplos.")
