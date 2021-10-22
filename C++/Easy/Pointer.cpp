// https://www.hackerrank.com/challenges/c-tutorial-pointer/problem

// The function is declared with a void return type, so there is no value to return.
// Modify the values in memory so that a contains their sum and b contains their absoluted difference.

#include <stdio.h>
#include <cmath>

void update(int *a,int *b) {
    int temp = *a + *b;
    *b = std::abs(*a - *b);
    *a = temp;
}

int main() {
    int a, b;
    int *pa = &a;
    int *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}