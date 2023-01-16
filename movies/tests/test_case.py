from django.test import TestCase


class YourTestClass(TestCase):

    def setUp(self):
        #Setup run before every test method.
        pass

    def tearDown(self):
        #Clean up run after every test method.
        # Este método no es particularmente útil para las pruebas de bases de datos,
        # ya que TestCase la clase base se encarga del desmontaje de la base de datos por usted.
        # ¿Dónde puede ser util? Eliminar ficheros, archivos multimedia
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)
