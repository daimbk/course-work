#include "FloatComplex.h"

// define constructor
FloatComplex::FloatComplex(float real_input, float imaginary_input)
    : IntComplex(static_cast<int>(real_input), static_cast<int>(imaginary_input)) // default constructor of parent class
{
    real = real_input;
    imaginary = imaginary_input;
}

// define operator overloads, returns complex number object
FloatComplex FloatComplex::operator+(const FloatComplex &object)
{
    // (a + bi) + (c + di)
    float real_sum = real + object.real;           // a + c
    float imag_sum = imaginary + object.imaginary; // b + d
    return FloatComplex(real_sum, imag_sum);
}

FloatComplex FloatComplex::operator-(const FloatComplex &object)
{
    // (a + bi) - (c + di)
    float real_diff = real - object.real;           // a - c
    float imag_diff = imaginary - object.imaginary; // b - d
    return FloatComplex(real_diff, imag_diff);
}

FloatComplex FloatComplex::operator*(const FloatComplex &object)
{
    // (a + bi) * (c + di)
    float real_mul = (real * object.real) - (imaginary * object.imaginary); // (a * c) - (b * d)
    float imag_mul = (real * object.imaginary) + (imaginary * object.real); // (a * d) + (b * c)
    return FloatComplex(real_mul, imag_mul);
}

FloatComplex FloatComplex::operator/(const FloatComplex &object)
{
    // (a + bi) / (c + di)
    float denom = (object.real * object.real) + (object.imaginary * object.imaginary); // (c^2 + d^2) is denominator
    float real_div = ((real * object.real) + (imaginary * object.imaginary)) / denom;  // ((a * c) + (b * d)) / (c^2 + d^2)
    float imag_div = ((imaginary * object.real) - (real * object.imaginary)) / denom;  // ((b * c) - (a * d)) / (c^2 + d^2)
    return FloatComplex(real_div, imag_div);
}

// getter functions
float FloatComplex::getReal() const
{
    return real;
}

float FloatComplex::getImaginary() const
{
    return imaginary;
}
