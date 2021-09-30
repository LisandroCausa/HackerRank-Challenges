# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)

    max_score = arr[0]
    runner_up_score = 0

    for i in arr:
        if i < max_score:
            runner_up_score = i
            print(runner_up_score)
            break