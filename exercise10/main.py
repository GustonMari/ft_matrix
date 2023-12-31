import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red

if __name__ == "__main__":
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(u.row_echelon())
    # [1.0, 0.0, 0.0]
    # [0.0, 1.0, 0.0]
    # [0.0, 0.0, 1.0]
    u = Matrix([
        [1., 2.],
        [3., 4.],
    ])
    print(u.row_echelon())
    # [1.0, 0.0]
    # [0.0, 1.0]
    u = Matrix([
        [1., 2.],
        [2., 4.],
    ])
    print(u.row_echelon())
    # [1.0, 2.0]
    # [0.0, 0.0]
    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ])
    print(u.row_echelon())
    # [1.0, 0.625, 0.0, 0.0, -12.1666667]
    # [0.0, 0.0, 1.0, 0.0, -3.6666667]
    # [0.0, 0.0, 0.0, 1.0, 29.5 ]
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    blue("row_echelon([[0, 0], [0, 0]])")
    u = Matrix([[0, 0], [0, 0]])
    green(f"Result :\n{u.row_echelon()}\n\nExpected :\n[[0, 0], [0, 0]]\n")

    blue("row_echelon([[1, 0], [0, 0]])")
    u = Matrix([[1, 0], [0, 1]])
    green(f"Result :\n{u.row_echelon()}\n\nExpected :\n[[1, 0], [0, 1]]\n")
    
    blue("row_echelon([[4, 2], [2, 1]])")
    u = Matrix([[4, 2], [2, 1]])
    green(f"Result :\n{u.row_echelon()}\n\nExpected :\n[[1, 0.5], [0, 0]]\n")
    
    blue("row_echelon([[-7, 2], [4, 8]])")
    u = Matrix([[-7, 2], [4, 8]])
    green(f"Result :\n{u.row_echelon()}\n\nExpected :\n[[1, 0], [0, 1]]\n")
    
    blue("row_echelon([[1, 2], [4, 8]])")
    u = Matrix([[1, 2], [4, 8]])
    green(f"Result :\n{u.row_echelon()}\n\nExpected :\n[[1, 2], [0, 0]]\n")
