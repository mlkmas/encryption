#include <iostream>
#include "Point.h"

int main() {
    // Creating points using both constructors
    Point p1;
    Point p2(3, 4);

    // Printing initial points
    std::cout << "Point p1: ";
    p1.print();

    std::cout << "Point p2: ";
    p2.print();

    // Setting new values for p1
    p1.setX(5);
    p1.setY(6);

    // Printing updated p1
    std::cout << "Updated Point p1: ";
    p1.print();
     std::cin.get(); 

    return 0;
}
