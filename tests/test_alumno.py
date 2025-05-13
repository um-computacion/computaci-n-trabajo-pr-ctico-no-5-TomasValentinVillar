import unittest
from src.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_crear_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.dni, "12345678")
        self.assertEqual(alumno.legajo, "A123")

    def test_repr_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Legajo: A123"
        self.assertEqual(str(alumno), expected)

    def test_legajo_vacio(self):
        with self.assertRaises(ValueError):
            alumno = Alumno("Juan", "Pérez", "12345678", "")

    def test_legajo_formato_invalido(self):
        with self.assertRaises(ValueError):
            alumno = Alumno("Juan", "Pérez", "12345678", "123")

    
    def test_herencia_pensar(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        alumno.pensar("Una idea estudiantil")
        self.assertEqual(alumno.pensamientos, 1)
        self.assertEqual(alumno.ultima_idea, "Una idea estudiantil")