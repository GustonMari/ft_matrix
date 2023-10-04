from vector import Vector
import sys
sys.path.append('../utils/')
from utils import custom_abs, custom_min, custom_max
# ! ------------------------------------------------------------MATRIX-----------------------------------------------------------------------------

class Matrix:
    
    # ? CONSTRUCTOR
    
    def __init__(self, data):
        self.data = data

    def __str__(self):
        x = '\n'.join([' '.join(['{:1}'.format(item) for item in row]) for row in self.data])
        return x

    def __iter__(self):
        return iter(self.data)
        
    def __mul__(self, other):
        """
        Element-wise multiplication of two matrices.
        """
        # if other is a scalar
        if not isinstance(other, Matrix):
            self.scl(other)
            return Matrix(self.data)
        # if other is a matrix
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
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value

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
                # if -0.0, it is converted to 0.0
                if self.data[row][column] * scalar == -0.0:
                    self.data[row][column] = 0.0
                else:
                    self.data[row][column] *= scalar

    def mul_vec(self, vector):
        """Multiply the matrix by a vector."""
        if len(self.data[0]) != len(vector.data):
            raise ValueError("Number of columns in the matrix must match the dimension of the vector.")

        result_data = [0 for elem in range(len(self.data))]

        for i in range(len(self.data)):
            for j in range(len(vector.data)):
                result_data[i] += self.data[i][j] * vector.data[j]

        return Vector(result_data)

    def mul_mat(self, other):
        """Multiply the matrix by another matrix."""
        if len(self.data[0]) != len(other.data):
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")

        result_data = [[0 for elem in range(len(other.data[0]))] for elem in range(len(self.data))]

        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    result_data[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(result_data)

    def trace(self):
        """compute the trace of a matrix, i.e. the sum of the diagonal elements."""
        if len(self.data) != len(self.data[0]):
            raise ValueError("The self.data must be square to compute its trace.")

        trace_value = sum(self.data[i][i] for i in range(len(self.data)))

        return trace_value

    def transpose(self):
        """compute the transpose of a matrix."""
        result_data = [[0 for elem in range(len(self.data))] for elem in range(len(self.data[0]))]

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result_data[j][i] = self.data[i][j]

        return Matrix(result_data)



# ! ------------------------------------------------------------ROW-----------------------------------------------------------------------------
    def find_pivot(self, row: int, column: int):
        zero = 0  # Default value for K
        custom_max_val = 0
        custom_max_row = row

        for row_index in range(row, len(self.data)):
            point = custom_abs(self[row_index][column])

            if self[row_index][column] != zero and point > custom_max_val:
                custom_max_val = point
                custom_max_row = row_index

        return (self[custom_max_row][column], custom_max_row)

    def _swap_rows(self, mtx, row1, row2):
        temp = mtx[row1]
        mtx[row1] = mtx[row2]
        mtx[row2] = temp
        return mtx

    def _row_substraction(self, mtx, actual_row, actual_col):
        for i in range(len(mtx)):
            if i != actual_row:
                # pivot is the first non-zero element in the row
                pivot = mtx[i][actual_col]
                # row substraction by a multiple of the pivot row + if the result is -0, it is converted to 0
                mtx[i] = [0. if elem - pivot * elem2 == -0 else elem - pivot * elem2 for elem, elem2 in zip(mtx[i], mtx[actual_row])]
        return mtx

    # * https://www.auto-math.be/public/8/module/16/theorie/65
    # * https://bouquinpython.readthedocs.io/fr/latest/matrices.html
    # * https://www.delftstack.com/fr/howto/python/gaussian-elicustom_mination-using-pivoting/
    # * http://desaintar.free.fr/python/cours/pivot.pdf
    def row_echelon(self):
        """Create a row echelon form of the matrix."""
        mtx = self.data
        row = len(mtx)
        column = len(mtx[0])
        actual_col = 0
        
        for actual_row in range(row):
            # row echelon form is completed
            if actual_col >= column:
                return mtx
            i = actual_row
            # finds a non-zero element in the current column.
            # This is necessary to locate a pivot element (the first non-zero element) for row operations.
            while mtx[i][actual_col] == 0:
                i += 1
                if i == row:
                    # find the next row with a non-zero element in the current column.
                    i = actual_row
                    actual_col += 1
                    # we've processed all columns, so we're done
                    if column == actual_col:
                        return mtx
            mtx = self._swap_rows(mtx, i, actual_row)
            # div is assigned the value of the pivot, the row is divided by the div to make the pivot element equal to 1
            # It's a crucial step in achieving the row echelon form.
            div = mtx[actual_row][actual_col]
            mtx[actual_row] = [0. if elem / div == -0 else elem / div for elem in mtx[actual_row]]
            mtx = self._row_substraction(mtx, actual_row, actual_col)
            actual_col += 1
        return mtx

    # is used in Laplace's formula, it permit to create a smaller matrix from the original matrix
    def custom_minor(self, row, col):
        """
        Compute the custom_minor of the matrix by removing the specified row and column.
        """
        return Matrix([[self.data[i][j] for j in range(len(self.data[0])) if j != col] for i in range(len(self.data)) if i != row])

    def derterminant(self):
        """
        Compute the derterminant of the matrix.
        """
        rows, cols = len(self.data), len(self.data[0])

        if rows != cols:
            raise ValueError("The matrix is not square.")
        
        # for matrix 1x1
        if rows == 1:
            return self.data[0][0]
        # for matrix 2x2
        elif rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        # for matrix 3x3 and more using the Laplace formula using the recursive method
        else:
            det = 0
            for col in range(cols):
                det += ((-1) ** col) * self.data[0][col] * self.custom_minor(0, col).derterminant()
            return det
    
    def _transpose(self):
        """compute the transpose of a matrix."""
        if len(self.data) == 1 and len(self.data[0]) == 1:
            return Matrix([[self.data[0][0]]])

        result_data = [[0 for elem in range(len(self.data))] for elem in range(len(self.data[0]))]

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result_data[j][i] = self.data[i][j]

        return Matrix(result_data)

    def inverse(self):
        """
        Compute the inverse of the matrix.
        """
        rows, cols = len(self.data), len(self.data[0])

        if rows != cols:
            raise ValueError("The matrix is not square.")

        det = self.derterminant()

        if det == 0:
            raise ValueError("The matrix is not invertible, because its derterminant is 0.")

        # for matrix 1x1
        if rows == 1:
            return Matrix([[1 / self.data[0][0]]])
        # for matrix 2x2
        elif rows == 2:
            return Matrix([[self.data[1][1] / det, -self.data[0][1] / det], [-self.data[1][0] / det, self.data[0][0] / det]])
        # for matrix 3x3 and more using the Laplace formula using the recursive method
        else:
            # [0. if elem - pivot * elem2 == -0 else elem - pivot * elem2 for elem, elem2 in zip(mtx[i], mtx[actual_row])]
            cofactor = Matrix([[((-1) ** (i + j)) * self.custom_minor(i, j).derterminant() for j in range(cols)] for i in range(rows)])
            adjugate = cofactor._transpose()
            # return (1 / det) * adjugate
            return  adjugate * (1 / det)
    
    def rank(self):
        """
        Compute the rank of the matrix.
        """
        row = len(self.data)
        col = len(self.data[0])
        size = 0
        # get the custom_max size of the custom_minor matrix
        if row <= col:
            size = row
        else:
            size = col
        mtx = self.row_echelon()
        rank = 0
        # check number of pivot that are not equal to 0
        for i in range(size):
            if mtx[i][i] != 0:
                rank += 1
        return rank
        