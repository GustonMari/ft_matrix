import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red

if __name__ == "__main__":
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    print(u.trace())
    # 2.0
    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.],
    ])
    print(u.trace())
    # 9.0
    u = Matrix([
        [-2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.],
    ])
    print(u.trace())
    # -21.0
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    blue("trace of [[0, 0], [0, 0]]")
    u = Matrix([[0, 0], [0, 0]])
    green(f"Result :\n{u.trace()}\n\nExpected :\n0\n")
    
    blue("trace of [[1, 0], [0, 0]]")
    u = Matrix([[1, 0], [0, 1]])
    green(f"Result :\n{u.trace()}\n\nExpected :\n2\n")
    
    blue("trace of [[1, 2], [3, 4]]")
    u = Matrix([[1, 2], [3, 4]])
    green(f"Result :\n{u.trace()}\n\nExpected :\n5\n")
    
    blue("trace of [[8, -7], [4, 2]]")
    u = Matrix([[8, -7], [4, 2]])
    green(f"Result :\n{u.trace()}\n\nExpected :\n10\n") 
    
    blue("trace of [[1, 0, 0], [0, 1, 0], [0, 0, 1]]")
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    green(f"Result :\n{u.trace()}\n\nExpected :\n3\n")