#ifndef INTCOMPLEX_H // wrapper to handle multiple header import errors
#define INTCOMPLEX_H

class IntComplex
{
private:
    int real;
    int imaginary;

public:
    // declare constructor
    IntComplex(int real_input, int imaginary_input);

    // declare overload arithmetic operators
    IntComplex operator+(const IntComplex &object);
    IntComplex operator-(const IntComplex &object);
    IntComplex operator*(const IntComplex &object);
    IntComplex operator/(const IntComplex &object);

    // getter functions
    int getReal() const;
    int getImaginary() const;
};

#endif
