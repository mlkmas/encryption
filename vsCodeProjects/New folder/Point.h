#ifndef POINT_H
#define POINT_H

#include <iostream>

class Point {
private:
    int x, y;

public:
    Point();
    Point(int x, int y);
    int getX() const;
    int getY() const;
    void setX(int x);
    void setY(int y);
    void print() const;
};

#endif // POINT_H
