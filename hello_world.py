import unittest

def new_func(name):
    return (f"Hallo {name}")

class TestClass(unittest.TestCase):
    def greetingsTest1(self):
        self.assertEqual(new_func("Noah"), "Hallo Noah")

if __name__ == '__main__':
    unittest.main()