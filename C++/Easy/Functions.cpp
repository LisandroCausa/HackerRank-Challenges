// https://www.hackerrank.com/challenges/c-tutorial-functions/problem

// Write a function int max_of_four(int a, int b, int c, int d) which returns the maximum of the four arguments it receives.

#include <iostream>
#include <cstdio>

int max_of_four(int a, int b, int c, int d)
{
    int numbers[4] = {a, b, c, d};
    int max;
    int length = sizeof(numbers)/sizeof(numbers[0]);
    for(int i = 0; i < length; i++)
    {
        if(max < numbers[i])
        {
            max = numbers[i];
        }
    }

    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}