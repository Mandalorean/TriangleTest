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

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1,1,2), 'Equilateral','1,1,1 should be equilateral (False Fail)')

    def testScaleneTriangleA(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(1,2,3), 'Scalene Triangle', '3,4,5 is a Scalene  triangle')

    def testIsocelesTriangleA(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(2,2,3), 'Isoceles Triangle', '3,4,5 is a Isoceles triangle')

    def testTriangleA(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(222,2,3), 'Scalene Triangle', ' valid values for triangle')

    def testTriangleB(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(22,0,3), 'Scalene Triangle', ' valid values for triangle')

    def testTriangleC(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(22,8,0), 'Scalene Triangle', ' valid values for triangle')

    def testTriangleD(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(-3,8,6), 'Scalene Triangle', ' valid values for triangle')

    def testTriangleE(self):
        from triangle import classifyTriangle
        self.assertEqual(classifyTriangle(one,8,6), 'Scalene Triangle', ' valid values for triangle')







if __name__ == '__main__':
    print('Running unit tests')

    unittest.main()












"""import unittest


class MyTestCase(unittest.TestCase):
    def test_scalene_right(self):
        from triangle import classifyTriangle

        self.assertEqual(classifyTriangle(3,4,5),"Scalene right triangle")


    def test_scalene(self):
        from triangle import classifyTriangle

        self.assertEqual(classifyTriangle(3,4,6),"Scalene triangle")


    def test_isoceles(self):
        from triangle import classifyTriangle

        self.assertEqual(classifyTriangle(4,4,5),"Isosceles triangle")


    def test_equilateral(self):
        from triangle import classifyTriangle

        self.assertEqual(classifyTriangle(5,5,5),"Equilateral triangle")


    def test_false_triangle(self):
        from triangle import classifyTriangle

        self.assertEqual(classifyTriangle(0,4,5),"Invalid triangle")

    def test_triangle(self):
        from triangle import classifyTriangle

        self.assertEqual(classifyTriangle(4,0,5),"Invalid triangle")







if __name__ == '__main__':
    unittest.main()
"""