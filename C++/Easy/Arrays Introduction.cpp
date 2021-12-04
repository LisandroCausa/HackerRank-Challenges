// https://www.hackerrank.com/challenges/arrays-introduction/problem

// You will be given an array of N integers and you have to print the integers in the reverse order.

#include <iostream>

int main() 
{
    int size;
    std::cin >> size;
    int* array = new int[size];
    for(int i = 0; i < size; i++)
    {
        std::cin >> array[i];
    }

    for(int i = size-1; i >= 0; i--)
    {
        std::cout << array[i] << " ";
    }
    delete[] array;
    return 0;
}