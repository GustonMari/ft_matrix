import sys
sys.path.append('../exercise00/')
from vector import Vector

def cross_product(u, v):
    if not isinstance(u, Vector) or not isinstance(v, Vector):
            raise ValueError("Both vectors must be of type Vector.")

    # result_x = u.y * v.z - u.z * v.y
    # result_y = u.z * v.x - u.x * v.z
    # result_z = u.x * v.y - u.y * v.x
    
    result_x = u[1] * v[2] - u[2] * v[1]
    result_y = u[2] * v[0] - u[0] * v[2]
    result_z = u[0] * v[1] - u[1] * v[0]

    return Vector([result_x, result_y, result_z])