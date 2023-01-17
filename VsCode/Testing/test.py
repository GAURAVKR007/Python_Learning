import unittest

import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print("Testing Started...")

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        test_param = 'Hihihi'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result,"Enter a Number")

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result,"Enter a Number")
    
    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result,"Enter a Number")

    def tearDown(self):
        print("Testing Done")

if __name__ == '__main__':
    unittest.main() 


    # Run it in Terminal => python -m unittest -v