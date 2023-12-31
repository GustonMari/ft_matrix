import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red

if __name__ == "__main__":
    u = Matrix([
        [ 1., -1.],
        [-1., 1.],
    ])
    print(u.derterminant())
    # 0.0
    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.],
    ])
    print(u.derterminant())
    # 8.0
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ])
    print(u.derterminant())
    # -174.0
    u = Matrix([
        [ 8., 5., -2., 4.],
        [ 4., 2.5, 20., 4.],
        [ 8., 5., 1., 4.],
        [28., -4., 17., 1.],
    ])
    print(u.derterminant())
    # 1032
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    blue("derterminant([[0, 0], [0, 0]])")
    u = Matrix([[0, 0], [0, 0]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n0\n")
    
    blue("derterminant([[1, 0], [0, 1]])")
    u = Matrix([[1, 0], [0, 1]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n1\n")
    
    blue("derterminant([[2, 0], [0, 2]])")
    u = Matrix([[2, 0], [0, 2]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n4\n")
    
    blue("derterminant([[1, 1], [1, 1]])")
    u = Matrix([[1, 1], [1, 1]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n0\n")
    
    blue("derterminant([[0, 1], [1, 0]])")
    u = Matrix([[0, 1], [1, 0]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n-1\n")
    
    blue("derterminant([[1, 2], [3, 4]])")
    u = Matrix([[1, 2], [3, 4]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n-2\n")
    
    blue("derterminant([[-7, 5], [4, 6]])")
    u = Matrix([[-7, 5], [4, 6]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n-62\n")
    
    blue("derterminant([[1, 0, 0], [0, 1, 0], [0, 0, 1]])")
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    green(f"Result :\n{u.derterminant()}\n\nExpected :\n1\n")
    