// https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem

// Input consists of the following space-separated values: int, long, char, float, and double, respectively.
// Print each element on a new line in the same order it was received as input. 
// Note that the floating point value should be correct up to 3 decimal places and the double to 9 decimal places.

#include <iostream>
#include <cstdio>

int main() {
    int a;
    long b;
    char c;
    float d;
    double e;

    std::cin >> a >> b >> c >> d >> e;

    std::cout << a << std::endl; 
    std::cout << b << std::endl; 
    std::cout << c << std::endl;
    std::cout.precision(3);
    std::cout << std::fixed << d << std::endl;
    std::cout.precision(9);
    std::cout << std::fixed << e;

    return 0;
}