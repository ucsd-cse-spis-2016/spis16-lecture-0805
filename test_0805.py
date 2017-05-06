import unittest
from depth import Hamming

class Test_Hamming(unittest.TestCase):

    def test_differentLengths(self):
        self.assertEqual(Hamming('1111','1'),-1)

    def test_0(self):
        self.assertEqual(Hamming('1111','1111'),0)



if __name__=='__main__':
    unittest.main()
