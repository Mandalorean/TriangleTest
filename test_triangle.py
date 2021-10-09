#check if the triangle is equilateral, isoceles, scalene or right
def classify_triangle(side_a,side_b,side_c):

    # require that the input values be >= 0 and <= 200
    if side_a>=200 or side_b>=200 or side_c>=200:
        return'InvalidInput'

    if side_a<=0 or side_b<=0 or side_c<=0:
        return'InvalidInput'

    if not (isinstance(side_a,int) and isinstance(side_b,int) and isinstance(side_c,int)):
        return'InvalidInput'

    if (side_a>=(side_b+side_c)) and (side_b>=(side_a+side_c)) and (side_c>=(side_a+side_b)):
        return'NotATriangle'

    if side_a==side_b and side_c==side_a and side_b==side_c:
        return'Equilateral'

    if ((side_a**2) + (side_b**2)) == (side_c**2) \
            or ((side_c**2) + (side_b**2)) == (side_a**2) \
            or ((side_a**2) + (side_c**2)) == (side_b**2):

        if side_b not in (side_a, side_c) and\
                side_a not in (side_b, side_c) and\
                side_c not in (side_a, side_b):
            return'Scalene Right Triangle'
        else:
            return 'Isoceles Right Triangle'

    if side_b not in (side_a, side_c) and\
        side_a not in (side_b, side_c) and\
        side_c not in (side_a, side_b):
        return'Scalene Triangle'
    else:
        return 'Isoceles Triangle'




if __name__=='__main__':
    # examples of running the code
    print(f'{classify_triangle(4,5,3)}')












