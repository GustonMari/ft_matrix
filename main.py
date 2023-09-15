from exercise00 import Vector, Matrix
from utils import *


if __name__ == "__main__":
    green("--------------------------------------EXERCISE00--------------------------------------------")
    blue("\n_____________________VECTOR_____________________\n")
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([4, 5, 6])
    vector3 = Vector([7, 8, 9, 10])
    yellow("A - Add two vectors together.")
    print(vector1,"+",vector2,"=", vector1.add(vector2))
    # ! raise an ValueError
    # print(vector1,"+",vector3,"=", vector1.add(vector3))
    yellow("B - Substract two vectors together.")
    print(vector1,"-",vector2,"=", vector1.sub(vector2))
    # ! raise an ValueError
    # print(vector1,"-",vector3,"=", vector1.sub(vector3))
    yellow("c - multiply vector by a scalar factor")
    print(vector1,"*",9,"=", vector1.scl(9))
    # ! raise an ValueError
    # print(vector1,"-",vector3,"=", vector1.scl(vector3))
    blue("\n_____________________MATRIX_____________________\n")
    
    matrice1 = Matrix([[1, 2, 3], [4, 5, 6]])
    
    print(matrice1)