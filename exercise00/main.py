from vector import Vector
from matrix import Matrix
import sys
sys.path.append('../utils/')
# Now you can import your module
from utils import green, blue, yellow, red


if __name__ == "__main__":
    green("--------------------------------------EXERCISE00--------------------------------------------")
    blue("\n_____________________VECTOR_____________________\n")
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([4, 5, 6])
    vector3 = Vector([7, 8, 9, 10])
    yellow("A - Add two vectors together.")
    vector1.add(vector2)
    print(vector1)
    # ! raise an ValueError
    # print(vector1.add(vector3))
    yellow("B - Substract two vectors together.")
    vector1.sub(vector2)
    print(vector1)
    # ! raise an ValueError
    # print(vector1.sub(vector3))
    yellow("c - multiply vector by a scalar factor")
    vector1.scl(9)
    print(vector1)
    # ! raise an ValueError
    # print(vector1.scl(vector3))
    blue("\n_____________________MATRIX_____________________\n")
    
    matrice1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrice2 = Matrix([[7, 8, 9], [10, 11, 12]])
    matrice3 = Matrix([[13, 14, 15], [16, 17, 18], [19, 20, 21]])
    
    yellow("\nA - Add two matrices together.\n")
    print(matrice1, "\n--------------")
    matrice1.add(matrice2)
    print(matrice1)
    # ! raise an ValueError
    # matrice1.add(matrice3)

    yellow("\nB - Substract two matrices together.\n")
    print(matrice1, "\n--------------")
    matrice1.sub(matrice2)
    print(matrice1)
    # ! raise an ValueError
    # matrice1.sub(matrice3)
    
    yellow("\nC - Multiply a matrices by a scalar.\n")
    print(matrice1, "\n--------------")
    matrice1.scl(2)
    print(matrice1)
    
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------")
    u = Vector([0, 0])
    v = Vector([0, 0])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    blue("'[1, 0]' and '[0, 1]")
    u = Vector([1, 0])
    v = Vector([0, 1])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n[1, 1]\n")

    blue("'[1, 1]' and '[1, 1]")
    u = Vector([1, 1])
    v = Vector([1, 1])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n[2, 2]\n")

    blue("'[21, 21]' and '[21, 21]")
    u = Vector([21, 21])
    v = Vector([21, 21])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n[42, 42]\n")

    blue("'[-21, 21]' and '[21, -21]")
    u = Vector([-21, 21])
    v = Vector([21, -21])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    blue("'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]")
    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n[9, 9, 9, 9, 9, 9, 9, 9, 9, 9]\n")

    yellow("\n--------------------MATRIX-----------------------------------\n")

    blue("'[[0, 0], [0, 0]]' and '[[0, 0], [0, 0]]")
    u = Matrix([[0, 0], [0, 0]])
    v = Matrix([[0, 0], [0, 0]])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")

    blue("'[[1, 0], [0, 1]]' and '[[0, 0], [0, 0]]")
    u = Matrix([[1, 0], [0, 1]])
    v = Matrix([[0, 0], [0, 0]])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n1 0\n0 1\n")

    blue("'[[1, 1], [1, 1]]' and '[[1, 1], [1, 1]]")
    u = Matrix([[1, 1], [1, 1]])
    v = Matrix([[1, 1], [1, 1]])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n2 2\n2 2\n")

    blue("'[[21, 21], [21, 21]]' and '[[21, 21], [21, 21]]")
    u = Matrix([[21, 21], [21, 21]])
    v = Matrix([[21, 21], [21, 21]])
    u.add(v)
    green(f"Result : \n{u}\n\nExpected :\n42 42\n42 42\n")

    yellow("SUB\n")

    yellow("\nvector\n")

    blue("'[0, 0]' sub '[0, 0]")
    u = Vector([0, 0])
    v = Vector([0, 0])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    blue("'[1, 0]' sub '[0, 1]")
    u = Vector([1, 0])
    v = Vector([0, 1])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n[1, -1]\n")

    blue("'[1, 1]' sub '[1, 1]")
    u = Vector([1, 1])
    v = Vector([1, 1])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    blue("'[21, 21]' sub '[21, 21]")
    u = Vector([21, 21])
    v = Vector([21, 21])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    blue("'[-21, 21]' sub '[21, -21]")
    u = Vector([-21, 21])
    v = Vector([21, -21])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n[-42, 42]\n")

    blue("'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' sub '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]")
    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n[-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]\n")

    yellow("\nMATRIX\n")

    blue("'[[0, 0], [0, 0]]' sub '[[0, 0], [0, 0]]")
    u = Matrix([[0, 0], [0, 0]])
    v = Matrix([[0, 0], [0, 0]])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")

    blue("'[[1, 0], [0, 1]]' sub '[[0, 0], [0, 0]]")
    u = Matrix([[1, 0], [0, 1]])
    v = Matrix([[0, 0], [0, 0]])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n1 0\n0 1\n")

    blue("'[[1, 1], [1, 1]]' sub '[[1, 1], [1, 1]]")
    u = Matrix([[1, 1], [1, 1]])
    v = Matrix([[1, 1], [1, 1]])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")

    blue("'[[21, 21], [21, 21]]' sub '[[21, 21], [21, 21]]")
    u = Matrix([[21, 21], [21, 21]])
    v = Matrix([[21, 21], [21, 21]])
    u.sub(v)
    green(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")
