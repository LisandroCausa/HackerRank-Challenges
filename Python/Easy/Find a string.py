# https://www.hackerrank.com/challenges/find-a-string/problem

# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    count = 0
    string_fragment = ""
    for c in string:
        if len(string_fragment) >= len(sub_string):
            string_fragment = string_fragment[1:]
        string_fragment += c

        if sub_string == string_fragment:
            count += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)