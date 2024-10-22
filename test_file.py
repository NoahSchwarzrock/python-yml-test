import unittest
from hello_world import new_func

class TestClass(unittest.TestCase):
    def test_greetings1(self):
        self.assertEqual(new_func("Noah"), "Hallo Noah")
        
    def test_type_greetings1(self):
        self.assertEqual(type(new_func("Noah")), str)
        
if __name__ == '__main__':
    unittest.main()