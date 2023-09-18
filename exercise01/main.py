import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow
from linear_combination import linear_combination


if __name__ == "__main__":
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
    #  [10.]
    #  [-2.]
    #  [0.5]
    print(linear_combination([v1, v2], [10., -2.]))
    #  [10.]
    #  [0.]
    #  [230.]