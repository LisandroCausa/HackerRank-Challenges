# https://www.hackerrank.com/challenges/nested-list/problem

# Given the names and grades for each student in a class of N students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score,name])

    students.sort()
    lowest_value = students[0][0]
    second_lowest_value = 1000
    second_lowest_value_names = []
    
    for i in students:
        if i[0] > second_lowest_value:
            break
        elif i[0] > lowest_value:
            second_lowest_value = i[0]
            second_lowest_value_names.append(i[1])

    second_lowest_value_names.sort()
    for name in second_lowest_value_names:
        print(name)