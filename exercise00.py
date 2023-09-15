
# ! ------------------------------------------------------------VECTOR-----------------------------------------------------------------------------

class Vector:
    def __init__(self, data):
        """Constructor"""
        self.data = data
        
    def __str__(self):
        """Is used to see not the object but what is inside the data.
            Don't forget to cast into string"""
        return str(self.data)
    
    def add(self, other):
        """Add two vectors together."""
        
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be the same length.")
        
        result = [v1 + v2 for v1, v2 in zip(self.data, other.data)]
        return result

    def sub(self, other):
        """substract two vectors together."""
        
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be the same length.")
        
        result = [v1 - v2 for v1, v2 in zip(self.data, other.data)]
        return result

    def scl(self, scalar):
        """multiply vector by a scalar factor"""
        
        result = [v1 * scalar for v1 in self.data]
        return result

# ! ------------------------------------------------------------MATRIX-----------------------------------------------------------------------------

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.data])
        return x
    

