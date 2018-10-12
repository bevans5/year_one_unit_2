import random
my_nums = [1,2,3,4,5,6,7,8,9,10]

# access the 5th element in my_nums
# print(my_nums[4])

# create a sequential search function for my nums
def sequential_search(arr, target):
    ans = False
    for num in my_nums:
        if num == target:
            ans = True
    return ans
# Explain how a binary search would work on my_nums


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

# Spicy: print the entire middle row
# Spicy: print the first value of every row
# Spicy: take in two 2D arrays and find the middle value of both

# Iterating over 2D arrays
my_nums = [[random.randint(0,500) for col in range(5)] for row in range(3)]

# mild: print out every single value in my_nums

# medium: replace all noneven numbers in my_nums with 0

# spicy: find the highest number in my_nums

# spicy plus: find the mean for my_nums



# snail: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
# flatten: https://www.codewars.com/kata/flatten-and-sort-an-array
# lazy startup: https://www.codewars.com/kata/the-lazy-startup-office
