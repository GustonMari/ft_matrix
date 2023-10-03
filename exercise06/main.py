import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red
from cross_product import cross_product

if __name__ == "__main__":
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print(cross_product(u, v))
    # # [0.]
    # # [1.]
    # # [0.]
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(cross_product(u, v))
    # # [-3.]
    # # [6.]
    # # [-3.]
    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print(cross_product(u, v))
    # # [17.]
    # # [-58.]
    # # [-16.]
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    blue("cross product of [0, 0, 0] and [0, 0, 0]")
    u = Vector([0, 0, 0])
    v = Vector([0, 0, 0])
    green(f"Result :\n{cross_product(u, v)}\n\nExpected :\n[0, 0, 0]\n")
    
    blue("cross product of [1, 0, 0] and [0, 0, 0]")
    u = Vector([1, 0, 0])
    v = Vector([0, 0, 0])
    green(f"Result :\n{cross_product(u, v)}\n\nExpected :\n[0, 0, 0]\n")
    
    blue("cross product of [1, 0, 0] and [0, 1, 0]")
    u = Vector([1, 0, 0])
    v = Vector([0, 1, 0])
    green(f"Result :\n{cross_product(u, v)}\n\nExpected :\n[0, 0, 1]\n")
    
    blue("cross product of [8, 7, -4] and [3, 2, 1]")
    u = Vector([8, 7, -4])
    v = Vector([3, 2, 1])
    green(f"Result :\n{cross_product(u, v)}\n\nExpected :\n[15, -20, -5]\n")
    
    blue("cross product of [1, 1, 1] and [0, 0, 0]")
    u = Vector([1, 1, 1])
    v = Vector([0, 0, 0])
    green(f"Result :\n{cross_product(u, v)}\n\nExpected :\n[0, 0, 0]\n")
    
    blue("cross product of [1, 1, 1] and [1, 1, 1]")
    u = Vector([1, 1, 1])
    v = Vector([1, 1, 1])
    green(f"Result :\n{cross_product(u, v)}\n\nExpected :\n[0, 0, 0]\n")
