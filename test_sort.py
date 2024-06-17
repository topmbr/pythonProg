import unittest
from sort import sort_words

class TestSortWordsFunction(unittest.TestCase):

    def test_sort_words(self):
        # Обычное предложение
        self.assertEqual(sort_words("hello world from Python"), ['Python', 'from', 'hello', 'world'])
        # Предложение с символами
        self.assertEqual(sort_words("hello, world! from Python."), ['Python.', 'from', 'hello,', 'world!'])
        # Пустая строка и строка с пробелами
        self.assertEqual(sort_words(""), [])
        self.assertEqual(sort_words("    "), [])
        # Предложение с числами
        self.assertEqual(sort_words("hello 123 world 456"), ['123', '456', 'hello', 'world'])

if __name__ == "__main__":
    unittest.main()
