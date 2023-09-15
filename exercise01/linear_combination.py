def linear_combination(coefficients, vectors):
    if len(coefficients) != len(vectors):
        raise ValueError("Number of coefficients must match the number of vectors")
    
    result = [sum(c * v_i for c, v_i in zip(coefficients, vector)) for vector in zip(*vectors)]
    return result