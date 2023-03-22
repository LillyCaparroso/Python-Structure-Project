from unittest import TestCase

from app.app import App


class TestApp(TestCase):
    def testSaludo(self):
        app = App()
        self.assertEqual(app.saludo(), "saludo")
