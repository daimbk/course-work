#ifndef FLOATCOMPLEX_H // wrapper to handle multiple header import errors
#define FLOATCOMPLEX_H

#include "IntComplex.h"

class FloatComplex : public IntComplex // inherit from IntComplex
{
private:
    float real;
    float imaginary;

public:
    // declare constructor
    FloatComplex(float real_input, float imaginary_input);

    // declare overload arithmetic operators
    FloatComplex operator+(const FloatComplex &object);
    FloatComplex operator-(const FloatComplex &object);
    FloatComplex operator*(const FloatComplex &object);
    FloatComplex operator/(const FloatComplex &object);

    // getter functions
    float getReal() const;
    float getImaginary() const;
};

#endif
