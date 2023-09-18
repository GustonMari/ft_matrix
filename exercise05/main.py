import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow
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