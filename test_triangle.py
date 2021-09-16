import unittest
from triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral','1,1,1 should be equilateral')

    if __name__ == '__main__':    print('Running unit tests')
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