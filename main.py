from vector import Vector
from matrix import Matrix
from utils import *


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
    
    yellow("A - Add two matrices together.")
    print(matrice1, "\n--------------")
    matrice1.add(matrice2)
    print(matrice1)
    # ! raise an ValueError
    # matrice1.add(matrice3)