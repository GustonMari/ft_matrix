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
    v = Vector([4., 2.])
    print(u.mul_vec(v))
    # [4.]
    # [2.]
    u = Matrix([
        [2., 0.],
        [0., 2.],
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v))
    # [8.]
    # [4.]
    u = Matrix([
        [2., -2.],
        [-2., 2.],
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v))
    # [4.]
    # [-4.]
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    v = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    print(u.mul_mat(v))
    # [1., 0.]
    # [0., 1.]
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    v = Matrix([
        [2., 1.],
        [4., 2.],
    ])
    print(u.mul_mat(v))
    # [2., 1.]
    # [4., 2.]
    u = Matrix([
        [3., -5.],
        [6., 8.],
    ])
    v = Matrix([
        [2., 1.],
        [4., 2.],
    ])
    print(u.mul_mat(v))
    # [-14., -7.]
    # [44., 22.]
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    blue("linear_transformation([[0, 0], [0, 0]], [3, 7])")
    u = Matrix([[0, 0], [0, 0]])
    v = Vector([3, 7])
    green(f"Result :\n{u.mul_vec(v)}\n\nExpected :\n[0, 0]\n")
    
    blue("linear_transformation([[1, 0], [0, 1]], [3, 7])")
    u = Matrix([[1, 0], [0, 1]])
    v = Vector([3, 7])
    green(f"Result :\n{u.mul_vec(v)}\n\nExpected :\n[3, 7]\n")
    
    blue("linear_transformation([[1, 0], [0, 1]], [4, 2])")
    u = Matrix([[1, 1], [1, 1]])
    v = Vector([4, 2])
    green(f"Result :\n{u.mul_vec(v)}\n\nExpected :\n[6, 6]\n")
    
    blue("linear_transformation([[2, 0], [0, 2]], [2, 1])")
    u = Matrix([[2, 0], [0, 2]])
    v = Vector([2, 1])
    green(f"Result :\n{u.mul_vec(v)}\n\nExpected :\n[4, 2]\n")
    
    blue("linear_transformation([[0.5, 0], [0, 0.5]], [4, 2])")
    u = Matrix([[0.5, 0], [0, 0.5]])
    v = Vector([4, 2])
    green(f"Result :\n{u.mul_vec(v)}\n\nExpected :\n[2, 1]\n")