#include "IntComplex.h"

// define constructor
IntComplex::IntComplex(int real_input, int imaginary_input)
{
    real = real_input;
    imaginary = imaginary_input;
}

// define operator overloads, returns complex number object
IntComplex IntComplex::operator+(const IntComplex &object)
{
    // (a + bi) + (c + di)
    int real_sum = real + object.real;           // a + c
    int imag_sum = imaginary + object.imaginary; // b + d
    return IntComplex(real_sum, imag_sum);
}

IntComplex IntComplex::operator-(const IntComplex &object)
{
    // (a + bi) - (c + di)
    int real_diff = real - object.real;           // a - c
    int imag_diff = imaginary - object.imaginary; // b - d
    return IntComplex(real_diff, imag_diff);
}

IntComplex IntComplex::operator*(const IntComplex &object)
{
    // (a + bi) * (c + di)
    int real_mul = (real * object.real) - (imaginary * object.imaginary); // (a * c) - (b * d)
    int imag_mul = (real * object.imaginary) + (imaginary * object.real); // (a * d) + (b * c)
    return IntComplex(real_mul, imag_mul);
}

IntComplex IntComplex::operator/(const IntComplex &object)
{
    // (a + bi) / (c + di)
    int denom = (object.real * object.real) + (object.imaginary * object.imaginary); // (c^2 + d^2) is denominator
    int real_div = ((real * object.real) + (imaginary * object.imaginary)) / denom;  // ((a * c) + (b * d)) / (c^2 + d^2)
    int imag_div = ((imaginary * object.real) - (real * object.imaginary)) / denom;  // ((b * c) - (a * d)) / (c^2 + d^2)
    return IntComplex(real_div, imag_div);
}

// getter functions
int IntComplex::getReal() const
{
    return real;
}

int IntComplex::getImaginary() const
{
    return imaginary;
}
