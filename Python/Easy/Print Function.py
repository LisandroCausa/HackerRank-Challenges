# https://www.hackerrank.com/challenges/python-print/problem

# Print the list of integers from 1 through n as a string, without spaces.

if __name__ == '__main__':
    n = int(input())

    values = []

    for i in range(1, n + 1):
        values.append(i)

    print(*values, sep="") # Prints all values in the array of values without separations