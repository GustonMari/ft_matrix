import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red
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
    
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    blue("linear_combination([Vector([-42, 42])], [-1.])")
    result0 = linear_combination([Vector([-42, 42])], [-1.])
    green(f"Result :\n{result0}\n\nExpected :\n[42.0, -42.0]\n")

    blue("linear_combination([Vector([-42.]), Vector([-42.]), Vector([-42.])], [-1., 1., 0.])")
    result1 = linear_combination([Vector([-42.]), Vector([-42.]), Vector([-42.])], [-1., 1., 0.])
    green(f"Result :\n{result1}\n\nExpected :\n[0.0]\n")

    blue("linear_combination([Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.])")
    result2 = linear_combination([Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.])
    green(f"Result :\n{result2}\n\nExpected :\n[-62.0, -8.0]\n")

    blue("linear_combination([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.])")
    result3 = linear_combination([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.])
    green(f"Result :\n{result3}\n\nExpected :\n[-52.0, 70.0, -119.5]\n")
    