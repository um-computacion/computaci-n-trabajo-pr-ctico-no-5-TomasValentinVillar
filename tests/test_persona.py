import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")
    
    def test_repr_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)

    def test_pensar_incrementa_contador(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.ultima_idea, "Hola mundo")

    def test_pensar_con_tipo_invalido(self):
        persona = Persona("Juan", "Pérez", "12345678")
        with self.assertRaises(TypeError):
            persona.pensar(123)

    def test_pensar_con_cadena_vacia(self):
        persona = Persona("Juan", "Pérez", "12345678")
        with self.assertRaises(ValueError):
            persona.pensar("")
    def test_dni_vacio(self):
        with self.assertRaises(ValueError):
            persona = Persona("Juan", "Pérez", "")

    def test_dni_formato_invalido(self):
        with self.assertRaises(ValueError):
            persona = Persona("Juan", "Pérez", "123abc")

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            persona = Persona("", "Pérez", "12345678")

    def test_apellido_vacio(self):
        with self.assertRaises(ValueError):
            persona = Persona("Juan", "", "12345678")

    def test_pensar_none(self):
        persona = Persona("Juan", "Pérez", "12345678")
        with self.assertRaises(TypeError):
            persona.pensar(None)
    