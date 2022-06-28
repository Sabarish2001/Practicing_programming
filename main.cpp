#include<iostream>

using namespace std;

class Shape
{
public:

    virtual int area()=0;
    virtual int perimeter()=0;
};

class Rectangle : public Shape
{
public:
    int length;
    int breadth;

    Rectangle(int len,int bread){length=len;breadth=bread;}

    int area(){return length*breadth;}
    int perimeter(){return (2*(length+breadth));}

    friend ostream & operator<<(ostream &out,Rectangle &r);
};

ostream & operator<<(ostream &out,Rectangle &r)
{
    out<<"Length = "<<r.length<<"Breadth = "<<r.breadth;
    return out;
}

class Circle : public Shape
{
public:
    int radius;

    Circle(int rad){radius=rad;}

    int area(){return (3.145*radius*radius);}
    int perimeter(){return (2*3.145*radius);}

    friend ostream & operator<<(ostream &out,Circle &c);
};

ostream & operator<<(ostream &out,Circle &c)
{
    out<<"Radius = "<<c.radius;
    return out;
}

int main()
{
    Shape *s;
    Rectangle r(10,5);
    s=&r;
    cout<<"area of Rectangle = "<<s->area()<<endl;
    cout<<"perimeter of Rectangle = "<<s->perimeter()<<endl;
    cout<<r<<endl;

    Circle c(10);
    s=&c;
    cout<<"Area of Circle = "<<s->area()<<endl;
    cout<<"Perimeter of Circle = "<<s->perimeter()<<endl;
    cout<<c;
    return 0;


}

