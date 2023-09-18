
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


