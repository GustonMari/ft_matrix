import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red
from cos import angle_cos

if __name__ == "__main__":
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(angle_cos(u, v))
    #  1.0
    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(angle_cos(u, v))
    #  0.0
    u = Vector([-1., 1.])
    v = Vector([ 1., -1.])
    print(angle_cos(u, v))
    #  -1.0
    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(angle_cos(u, v))
    #  1.0
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(angle_cos(u, v))
    #  0.974631846
    
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    u = Vector([1, 0])
    v = Vector([0, 1])
    blue("cos of [1, 0] and [0, 1]")
    green(f"Result :\n{angle_cos(u, v)}\n\nExpected :\n0\n")
    
    u = Vector([8, 7])
    v = Vector([3, 2])
    blue("cos of [8, 7] and [3, 2]")
    green(f"Result :\n{angle_cos(u, v)}\n\nExpected :\n0.9914542955425437\n")
    
    u = Vector([1, 1])
    v = Vector([1, 1])
    blue("cos of [1, 1] and [1, 1]")
    green(f"Result :\n{angle_cos(u, v)}\n\nExpected :\n1\n")
    
    u = Vector([4, 2])
    v = Vector([1, 1])
    blue("cos of [4, 2] and [1, 1]")
    green(f"Result :\n{angle_cos(u, v)}\n\nExpected :\n0.9486832980505138\n")
    
    u = Vector([-7, 3])
    v = Vector([6, 4])
    blue("cos of [-7, 3] and [6, 4]")
    green(f"Result :\n{angle_cos(u, v)}\n\nExpected :\n-0.5462677805469223\n")