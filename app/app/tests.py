"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11) # irá testa se o resultado (primeiro parametro) condiz com o valor dado no segundo parametro
        