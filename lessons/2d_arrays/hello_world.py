import random
# list comp for 2D array
# sorted ints
sorted_matrix = [[col for col in range(6)] for row in range(10)]
# random ints
matrix = [[random.randint(0,100) for col in range(5)] for row in range(3)]
# access the number 0 in the first row
#print(sorted_matrix[0][0])
# access the last number in the last row
#print(sorted_matrix[-1][-1])
# save the middle col index value in a var
mid_col = len(sorted_matrix[0])//2
# save the middle row index value in a var
mid_row = len(sorted_matrix)//2
# access the middle number in the middle row
print(sorted_matrix[mid_row][mid_col])

# Mild: create a function that will take in a 2D array and find the middle value
def find_mid(matrix):
    mid_col = len(matrix[0])//2
    mid_row = len(matrix)//2
    print(matrix[mid_row][mid_col])
find_mid(matrix)
print(matrix)

# Spicy: print the entire mid row
# Spicy: print the
