// https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem

// For each integer n in the inclusive interval [a,b]:
//      If 1 < n < 9, then print the English representation of it in lowercase. That is "one" for 1, "two" for 2, and so on.
//      Else if n > 9 and it is an even number, then print "even".
//      Else if n > 9 and it is an odd number, then print "odd".

#include <iostream>
#include <cstdio>


void printNumber(int i)
{
    switch(i)
    {
        case 1:
            std::cout << "one" << std::endl;
            break;
        case 2:
            std::cout << "two" << std::endl;
            break;
        case 3:
            std::cout << "three" << std::endl;
            break;
        case 4:
            std::cout << "four" << std::endl;
            break;
        case 5:
            std::cout << "five" << std::endl;
            break;
        case 6:
            std::cout << "six" << std::endl;
            break;
        case 7:
            std::cout << "seven" << std::endl;
            break;
        case 8:
            std::cout << "eight" << std::endl;
            break;
        default:
            std::cout << "nine" << std::endl;
    }
}

int main() {
    int a;
    int b;

    std::cin >> a;
    std::cin >> b;

    for(int i = a; i < b+1; i++)
    {
        if(1 <= i && i <= 9)
        {
            printNumber(i);
        }
        else if(i > 9)
        {
            if(i % 2 == 0)
            {
                std::cout << "even" << std::endl;
            }
            else
            {
                std::cout << "odd" << std::endl;
            }
        }
    }

    return 0;
}