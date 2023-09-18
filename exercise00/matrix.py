
# ! ------------------------------------------------------------MATRIX-----------------------------------------------------------------------------

class Matrix:
    
    # ? CONSTRUCTOR
    
    def __init__(self, data):
        self.data = data

    def __str__(self):
        x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.data])
        return x

    def __iter__(self):
        return iter(self.data)
        
    def __mul__(self, other):
        """
        Element-wise multiplication of two matrices.
        """
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication.")

        result_data = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] * other.data[i][j])
            result_data.append(row)

        return Matrix(result_data)

    def __rmul__(self, scalar):
        # This handles the case where a scalar is on the left side of *
        return self * scalar
    
    def __add__(self, other):
        self.add(other)
        return self
    
    def __sub__(self, other):
        self.sub(other)
        return self

    # ? PRIVATE METHODS
    
    def _check_add_sub(self, other):
        # Get the dimensions of both matrices
        rows_a, cols_a = len(self.data), len(self.data[0])
        rows_b, cols_b = len(other.data), len(other.data[0])

        # Check if the dimensions match for addition
        return (rows_a == rows_b) and (cols_a == cols_b)

    
    # ? PUBLIC METHODS
    
    def add(self, other):
        """Add two Matrix"""
        if not(self._check_add_sub(other)):
            raise ValueError("Matrices must be the same size.")
        # iterate through rows
        for row in range(len(self.data)):
            # iterate through columns
            for column in range(len(self.data[0])):
                self.data[row][column] = self.data[row][column] + other.data[row][column]

    def sub(self, other):
        """Add two Matrix"""
        if not(self._check_add_sub(other)):
            raise ValueError("Matrices must be the same size.")
        # iterate through rows
        for row in range(len(self.data)):
            # iterate through columns
            for column in range(len(self.data[0])):
                self.data[row][column] = self.data[row][column] - other.data[row][column]

    def scl(self, scalar):
        """Multiply a matrix by a scalar"""
        
        # iterate through rows
        for row in range(len(self.data)):
            # iterate through columns
            for column in range(len(self.data[0])):
                self.data[row][column] = self.data[row][column] * scalar