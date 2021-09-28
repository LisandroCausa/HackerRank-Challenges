# https://www.hackerrank.com/challenges/list-comprehensions/problem

# You are given three integers x, y and z representing the dimensions of a cuboid along
# with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 
# 3D grid where the sum of i + j + k is not equal to n.

def give_options(value):
    return [o for o in range(0, value + 1)]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    X_options = give_options(x)
    Y_options = give_options(y)
    Z_options = give_options(z)

    arrays = [[i, j, k] for i in X_options for j in Y_options for k in Z_options]

    arrays_equal_to_n = [t for t in arrays if sum(t) != n]

    print(arrays_equal_to_n)