__author__ = 'lena'

# Create a matrix with a list of lists
matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]
print(len(matrix))

# Access elements using successive integer indices
print(matrix[0][3])

# Create sparse matrix with a dictionary
smatrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(len(smatrix))

# Access elements using tuples as key
print(smatrix[(0, 3)])

# Entries that doen't exist return an error
try:
    print(smatrix[(0, 4)])
except KeyError:
    print("KeyError")

# Use the alt verstion of the get method
print(smatrix.get((0, 4), 0))