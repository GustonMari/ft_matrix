
def angle_cos(u, v):
    """Returns the cosine of the angle between vectors u and v."""
    if u.norm() == 0 or v.norm() == 0:
        return 0
    return u.dot(v) / (u.norm() * v.norm())