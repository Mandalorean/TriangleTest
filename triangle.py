def classifyTriangle(a,b,c):
    """    Your correct code goes here...  Fix the faulty logic below until the code passes all of
     you test cases.This function returns a string with the type of triangle from three integer values    corresponding to the lengths of the three sides of the Triangle.
    return:        If all three sides are equal, return 'Equilateral'        If exactly one pair of sides are equal, return 'Isoceles'        If no pair of  sides are equal, return 'Scalene'        If not a valid triangle, then return 'NotATriangle'        If the sum of any two sides equals the squate of the third side, then return 'Right'
    BEWARE: there may be a bug or two in this code    """
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput';

    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'

    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
