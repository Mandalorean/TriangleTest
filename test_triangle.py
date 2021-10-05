import unittest
from triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def testScaleneRightTriangleA(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(3,4,5), 'Scalene Right Triangle', '3,4,5 is a Scalene Right triangle')

    def testScaleneRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4), 'Scalene Right Triangle','5,3,4 is a Scalene Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral','1,1,1 should be equilateral')

    

    def testScaleneTriangleA(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(1,2,3), 'Scalene Triangle', '3,4,5 is a Scalene  triangle')

   

 

 


    

    







if __name__ == '__main__':
    print('Running unit tests')

    unittest.main()












