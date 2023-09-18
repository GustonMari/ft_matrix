
def angle_cos(u, v):
    """Returns the cosine of the angle between vectors u and v."""
    return u.dot(v) / (u.norm() * v.norm())