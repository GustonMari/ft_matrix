import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix

def lerp(u, v, t):
    """
    Linear interpolation between two values u and v.
    """
    if type(u) != type(v):
        raise ValueError("Objects have different types.")
    if t < 0.0 or t > 1.0:
        raise ValueError("Interpolation factor t must be in the range [0, 1].")

    if isinstance(u, (float, int)):
        result = round((1 - t) * u + t * v, 1)
    elif isinstance(u, Vector):
        result = [round((1 - t) * x1 + t * x2, 1) for x1, x2 in zip(u, v)]
    elif isinstance(u, Matrix):
        result = []
        for i in range(len(u.data)):
            row = []
            for j in range(len(u.data[0])):
                interpolated_value = round((1 - t) * u.data[i][j] + t * v.data[i][j], 1)
                row.append(interpolated_value)
            result.append(row)
    return result