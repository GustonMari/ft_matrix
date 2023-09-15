
# ! ------------------------------------------------------------MATRIX-----------------------------------------------------------------------------

class Matrix:
    
    # ? CONSTRUCTOR
    
    def __init__(self, data):
        self.data = data

    def __str__(self):
        x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.data])
        return x

    # ? PRIVATE METHODS
    
    def _check_add_sub(self, other):
        # Get the dimensions of both matrices
        rows_a, cols_a = len(self.data), len(self.data[0])
        rows_b, cols_b = len(other.data), len(other.data[0])

        # Check if the dimensions match for addition
        return (rows_a == rows_b) and (cols_a == cols_b)

        # """Check if the matrix are the same size"""
        # if len(self.data) != len(other.data):
        #     raise ValueError("Matrices must be the same size.")
        # for row in range(len(self.data)):
        #     if len(self.data[row]) != len(other.data[row]):
        #         raise ValueError("Matrices must be the same size.")
    
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