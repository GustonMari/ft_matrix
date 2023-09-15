import sys
sys.path.append('../exercise00/')
from vector import Vector
from matrix import Matrix
sys.path.append('../utils/')
from utils import green, blue, yellow
import linear_combination


if __name__ == "__main__":
    blue("Hello World!")
    vector1 = Vector([1, 2, 3])
    print(vector1)