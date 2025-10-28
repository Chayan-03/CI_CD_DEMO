import unittest
from app import hellow_world
class TestApp(unittest.TestCase):
    def test_hellow_world(self):
        self.assertEqual(hellow_world(), "Hello, World!")
        
if __name__ == '__main__':
    unittest.main()