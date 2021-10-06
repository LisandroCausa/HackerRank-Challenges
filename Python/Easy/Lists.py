# https://www.hackerrank.com/challenges/python-lists/problem

# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    arr = []
    N = int(input())
    Commands = []
    for inp in range(N):
        Commands.append(input())

    for com in Commands:
        com = com.split(" ")
        if com[0] == "insert":
            arr.insert(int(com[1]), int(com[2]))
        elif com[0] == "print":
            print(arr)
        elif com[0] == "remove":
            arr.remove(int(com[1]))
        elif com[0] == "append":
            arr.append(int(com[1]))
        elif com[0] == "sort":
            arr.sort()
        elif com[0] == "pop":
            arr.pop()
        elif com[0] == "reverse":
            arr.reverse()