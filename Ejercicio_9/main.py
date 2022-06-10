import unittest
from Palindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    __palindromo = None
    __notPalindromo = None

    def setUp(self):
        self.__palindromo = Palindromo("neuquen")
        self.__notPalindromo = Palindromo("hola")

    def testPalindromo(self):
        self.assertTrue(self.__palindromo.esPalindromo())

    def testNotPalindromo(self):
        self.assertFalse(self.__notPalindromo.esPalindromo())

if __name__ == "__main__":
    unittest.main()
