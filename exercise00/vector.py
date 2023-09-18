
# ! ------------------------------------------------------------VECTOR-----------------------------------------------------------------------------

class Vector:
    def __init__(self, data):
        """Constructor"""
        self.data = data
        
    def __str__(self):
        """Is used to see not the object but what is inside the data.
            Don't forget to cast into string"""
        return str(self.data)
    
    def __iter__(self):
        """Is used to iterate over the data"""
        return iter(self.data)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            result_data = [x * scalar for x in self.data]
            result = Vector(result_data)
            return result
        else:
            raise ValueError("Unsupported operand type for multiplication")

    def __rmul__(self, scalar):
        # This handles the case where a scalar is on the left side of *
        return self * scalar
    
    def __add__(self, other):
        self.add(other)
        return self
    
    def __sub__(self, other):
        self.sub(other)
        return self
    
    def add(self, other):
        """Add two vectors together."""
        
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be the same length.")
        
        self.data = [v1 + v2 for v1, v2 in zip(self.data, other.data)]

    def sub(self, other):
        """substract two vectors together."""
        
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be the same length.")
        
        self.data = [v1 - v2 for v1, v2 in zip(self.data, other.data)]

    def scl(self, scalar):
        """multiply vector by a scalar factor"""
        
        self.data = [v1 * scalar for v1 in self.data]
        
    def dot(self, other):
        """Dot product of two vectors."""
        
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be the same length.")
        # self.data = sum([v1 * v2 for v1, v2 in zip(self.data, other.data)])
        return sum([v1 * v2 for v1, v2 in zip(self.data, other.data)])


