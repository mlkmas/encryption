#include "Point.h"

// Default constructor
Point::Point() : x(0), y(0) {}

// Parameterized constructor
Point::Point(int x, int y) : x(x), y(y) {}

// Get x-coordinate
int Point::getX() const {
    return x;
}

// Get y-coordinate
int Point::getY() const {
    return y;
}

// Set x-coordinate
void Point::setX(int x) {
    this->x = x;
}

// Set y-coordinate
void Point::setY(int y) {
    this->y = y;
}

// Print point coordinates
void Point::print() const {
    std::cout << "(" << x << ", " << y << ")" << std::endl;
}
