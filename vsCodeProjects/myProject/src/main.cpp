#include <iostream>
#include "myheader.h"

void myFunction() {
    std::cout << "Hello from myFunction!" << std::endl;
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    myFunction();
    return 0;
}
