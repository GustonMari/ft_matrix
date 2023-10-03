import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow, red

if __name__ == "__main__":
    u = Vector([0., 0., 0.])
    print(u.norm_1(), u.norm(), u.norm_inf())
    # 0.0, 0.0, 0.0
    u = Vector([1., 2., 3.])
    print(u.norm_1(), u.norm(), u.norm_inf())
    # 6.0, 3.74165738, 3.0
    u = Vector([-1., -2.])
    print(u.norm_1(), u.norm(), u.norm_inf())
    # 3.0, 2.236067977, 2.0
    red("\n\n--------------------------------CORRECTION TEST--------------------------------------------\n\n")
    yellow("Norm\n")
    
    v1 = Vector([0])
    result = v1.norm()
    blue(f"\nNorm of {v1.data}:")
    green(f"\nResult :\n{result}\n\nExpected :\n0")

    v2 = Vector([1])
    result = v2.norm()
    blue(f"\nNorm of {v2.data}:")
    green(f"\nResult :\n{result}\n\nExpected :\n1.0")

    v3 = Vector([0, 0])
    result = v3.norm()
    blue(f"\nNorm of {v3.data}:")
    green(f"\nResult :\n{result}\n\nExpected :\n0.0")

    v4 = Vector([1, 0])
    result = v4.norm()
    blue(f"\nNorm of {v4.data}:")
    green(f"\nResult :\n{result}\n\nExpected :\n1.0")

    v5 = Vector([2, 1])
    result = v5.norm()
    blue(f"\nNorm of {v5.data}:")
    green(f"\nResult :\n{result}\n\nExpected :\n2.236067977")

    v6 = Vector([4, 2])
    result = v6.norm()
    blue(f"\nNorm of {v6.data}:")
    green(f"\nResult :\n{result}\n\nExpected :\n4.472135955")

    v7 = Vector([-4, -2])
    result = v7.norm()
    blue(f"\nNorm of {v7.data}:")
    green(f"\nResult :\n{result}\n\nExpected :\n4.472135955")

    yellow("\nNorm_1\n")

    v1 = Vector([0])
    result = v1.norm_1()
    blue(f"\nNorm_1 of {v1.data}")
    green(f"\nResult :\n{result}\n\nExpected :\n0")

    v2 = Vector([1])
    result = v2.norm_1()
    blue(f"\nNorm_1 of {v2.data}")
    green(f"\nResult :\n{result}\n\nExpected :\n1.0")

    v3 = Vector([0, 0])
    result = v3.norm_1()
    blue(f"\nNorm_1 of {v3.data}")
    green(f"\nResult :\n{result}\n\nExpected :\n0.0")

    v4 = Vector([1, 0])
    result = v4.norm_1()
    blue(f"\nNorm_1 of {v4.data}")
    green(f"\nResult :\n{result}\n\nExpected :\n1.0")

    v5 = Vector([2, 1])
    result = v5.norm_1()
    blue(f"\nNorm_1 of {v5.data}")
    green(f"\nResult :\n{result}\n\nExpected :\n3.0")

    v6 = Vector([4, 2])
    result = v6.norm_1()
    blue(f"\nNorm_1 of {v6.data}")
    green(f"\nResult :\n{result}\n\nExpected :\n6.0")

    v7 = Vector([-4, -2])
    result = v7.norm_1()
    blue(f"\nNorm_1 of {v7.data}")
    green(f"\nResult :\n{result}\n\nExpected :\n6.0")
