import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red


if __name__ == "__main__":
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    green(f"{u.dot(v)}")
    # 0.0
    u = Vector([1., 1.])
    v = Vector([1., 1.])
    green(f"{u.dot(v)}")
    # 2.0
    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    green(f"{u.dot(v)}")
    # 9.0
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    v1 = Vector([0, 0])
    v2 = Vector([0, 0])
    result = v1.dot(v2)
    blue(f"dot({v1.data}, {v2.data}")
    green(f"Result :\n{result}\n\nExpected :\n0")

    v1 = Vector([1, 0])
    v2 = Vector([0, 0])
    result = v1.dot(v2)
    blue(f"dot({v1.data}, {v2.data}")
    green(f"Result :\n{result}\n\nExpected :\n0\n")

    v1 = Vector([1, 0])
    v2 = Vector([1, 0])
    result = v1.dot(v2)
    blue(f"dot({v1.data}, {v2.data}")
    green(f"Result :\n{result}\n\nExpected :\n1\n")

    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    result = v1.dot(v2)
    blue(f"dot({v1.data}, {v2.data}")
    green(f"Result :\n{result}\n\nExpected :\n0\n")

    v1 = Vector([1, 1])
    v2 = Vector([1, 1])
    result = v1.dot(v2)
    blue(f"dot({v1.data}, {v2.data}")
    green(f"Result :\n{result}\n\nExpected :\n2\n")

    v1 = Vector([4, 2])
    v2 = Vector([2, 1])
    result = v1.dot(v2)
    blue(f"dot({v1.data}, {v2.data}")
    green(f"Result :\n{result}\n\nExpected :\n10\n")