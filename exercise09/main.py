import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow

if __name__ == "__main__":
    u = Matrix([
        [5., 2.],
        [0., 1.],
    ])
    print(u.transpose(), "\n")
    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.],
    ])
    print(u.transpose(), "\n")
    u = Matrix([
        [-2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.],
    ])
    print(u.transpose(), "\n")
    u = Matrix([
        [1., 2., 3., 4.],
        [5., 6., 7., 8.],
    ])
    print(u.transpose(), "\n")