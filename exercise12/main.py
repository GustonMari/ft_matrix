import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow

if __name__ == "__main__":
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(u.inverse())
    # [1.0, 0.0, 0.0]
    # [0.0, 1.0, 0.0]
    # [0.0, 0.0, 1.0]
    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.],
    ])
    print(u.inverse())
    # [0.5, 0.0, 0.0]
    # [0.0, 0.5, 0.0]
    # [0.0, 0.0, 0.5]
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ])
    print(u.inverse())
    # [0.649425287, 0.097701149, -0.655172414]
    # [-0.781609195, -0.126436782, 0.965517241]
    # [0.143678161, 0.074712644, -0.206896552]