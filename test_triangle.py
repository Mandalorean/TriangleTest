import unittest
from triangle import classify_triangle

class TestTriangles(unittest.TestCase):

    def testScaleneRightTriangleA(self):
        from triangle import classify_triangle
        self.assertEqual(classify_triangle(3,4,5), 'Scalene Right Triangle', '3,4,5 is a Scalene Right triangle')

    def testScaleneRightTriangleB(self):
        self.assertEqual(classify_triangle(5,3,4), 'Scalene Right Triangle','5,3,4 is a Scalene Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1,1,1), 'Equilateral','1,1,1 should be equilateral')



    def testScaleneTriangleA(self):
        from triangle import classify_triangle
        self.assertEqual(classify_triangle(1,2,3), 'Scalene Triangle', '3,4,5 is a Scalene  triangle')

    def testIsocelesTriangleA(self):
        from triangle import classify_triangle
        self.assertEqual(classify_triangle(2,2,3), 'Isoceles Triangle', '3,4,5 is a Isoceles triangle')

    def testTriangleA(self):
        from triangle import classify_triangle
        self.assertEqual(classify_triangle(222,2,3), 'InvalidInput', ' valid values for triangle')

    def testTriangleB(self):
        from triangle import classify_triangle
        self.assertEqual(classify_triangle(22,0,3), 'InvalidInput', ' valid values for triangle')

    def testTriangleC(self):
        from triangle import classify_triangle
        self.assertEqual(classify_triangle(22,8,0), 'InvalidInput', ' valid values for triangle')

    def testTriangleD(self):
        from triangle import classify_triangle
        self.assertEqual(classify_triangle(-3,8,6), 'InvalidInput', ' valid values for triangle')









if __name__ == '__main__':
    print('Running unit tests')

    unittest.main()











