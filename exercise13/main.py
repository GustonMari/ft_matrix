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
    print(u.rank())
    #  3
    u = Matrix([
        [ 1., 2., 0., 0.],
        [ 2., 4., 0., 0.],
        [-1., 2., 1., 1.],
    ])
    print(u.rank())
    #  2
    u = Matrix([
        [ 8., 5., -2.],
        [ 4., 7., 20.],
        [ 7., 6., 1.],
        [21., 18., 7.],
    ])
    print(u.rank())
    #  3
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    blue("rank([[0, 0], [0, 0]])")
    u = Matrix([[0, 0], [0, 0]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n0\n")
    
    blue("rank([[1, 0], [0, 1]])")
    u = Matrix([[1, 0], [0, 1]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n1\n")
    
    blue("rank([[2, 0], [0, 2]])")
    u = Matrix([[2, 0], [0, 2]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n2\n")
    
    blue("rank([[1, 1], [1, 1]])")
    u = Matrix([[1, 1], [1, 1]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n1\n")
    
    blue("rank([[0, 1], [1, 0]])")
    u = Matrix([[0, 1], [1, 0]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n2\n")
    
    blue("rank([[1, 2], [3, 4]])")
    u = Matrix([[1, 2], [3, 4]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n2\n")
    
    blue("rank([[-7, 5], [4, 6]])")
    u = Matrix([[-7, 5], [4, 6]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n2\n")
    
    blue("rank([[1, 0, 0], [0, 1, 0], [0, 0, 1]])")
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    green(f"Result :\n{u.rank()}\n\nExpected :\n3\n")