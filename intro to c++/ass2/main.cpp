#include <iostream>
#include "IntComplex.h"
#include "FloatComplex.h"

using std::cout, std::cin, std::endl, std::abs;

int main(int argc, char *argv[])
{
    // run if 8 numbers are entered to make 4 points
    if (argc < 8)
    {
        std::cout << "Incorrect. Enter 4 integers and 4 floats for 2 each complex numbers." << std::endl;
        return 1;
    }

    // access command line arguments and convert to integer and floats
    int real_int = std::stoi(argv[1]);
    int imag_int = std::stoi(argv[2]);
    int real2_int = std::stoi(argv[3]);
    int imag2_int = std::stoi(argv[4]);

    float real_f = std::stof(argv[5]);
    float imag_f = std::stof(argv[6]);
    float real2_f = std::stof(argv[7]);
    float imag2_f = std::stof(argv[8]);

    IntComplex intComplex_num1(real_int, imag_int);   // create intComplex object 1
    IntComplex intComplex_num2(real2_int, imag2_int); // create intComplex object 2

    FloatComplex floatComplex_num1(real_f, imag_f);   // create floatComplex object 1
    FloatComplex floatComplex_num2(real2_f, imag2_f); // create floatComplex object 2

    // Print all 4 complex numbers
    // .getImaginary() >= 0 ? " + " : " - " this check prints proper sign value of imag number
    // abs(imag) prints it as pos as sign is printing before already
    cout << "Complex numbers entered are:" << endl;
    cout << intComplex_num1.getReal() << (intComplex_num1.getImaginary() >= 0 ? " + " : " - ") << abs(intComplex_num1.getImaginary()) << "i" << endl;
    cout << intComplex_num2.getReal() << (intComplex_num2.getImaginary() >= 0 ? " + " : " - ") << abs(intComplex_num2.getImaginary()) << "i" << endl;
    cout << floatComplex_num1.getReal() << (floatComplex_num1.getImaginary() >= 0 ? " + " : " - ") << abs(floatComplex_num1.getImaginary()) << "i" << endl;
    cout << floatComplex_num2.getReal() << (floatComplex_num2.getImaginary() >= 0 ? " + " : " - ") << abs(floatComplex_num2.getImaginary()) << "i" << endl;

    cout << endl;

    // arithmetic operations
    // addition
    IntComplex int_sum = intComplex_num1 + intComplex_num2;
    FloatComplex float_sum = floatComplex_num1 + floatComplex_num2;
    cout << "Sum of IntComplex numbers: " << int_sum.getReal() << (int_sum.getImaginary() >= 0 ? " + " : " - ") << abs(int_sum.getImaginary()) << "i" << endl;
    cout << "Sum of FloatComplex numbers: " << float_sum.getReal() << (float_sum.getImaginary() >= 0 ? " + " : " - ") << abs(float_sum.getImaginary()) << "i" << endl;

    cout << endl;

    // subtraction
    IntComplex int_diff = intComplex_num1 - intComplex_num2;
    FloatComplex float_diff = floatComplex_num1 - floatComplex_num2;
    cout << "Difference of IntComplex numbers: " << int_diff.getReal() << (int_diff.getImaginary() >= 0 ? " + " : " - ") << abs(int_diff.getImaginary()) << "i" << endl;
    cout << "Difference of FloatComplex numbers: " << float_diff.getReal() << (float_diff.getImaginary() >= 0 ? " + " : " - ") << abs(float_diff.getImaginary()) << "i" << endl;

    cout << endl;

    // multiplication
    IntComplex int_mul = intComplex_num1 * intComplex_num2;
    FloatComplex float_mul = floatComplex_num1 * floatComplex_num2;
    cout << "Product of IntComplex numbers: " << int_mul.getReal() << (int_mul.getImaginary() >= 0 ? " + " : " - ") << abs(int_mul.getImaginary()) << "i" << endl;
    cout << "Product of FloatComplex numbers: " << float_mul.getReal() << (float_mul.getImaginary() >= 0 ? " + " : " - ") << abs(float_mul.getImaginary()) << "i" << endl;

    cout << endl;

    // division
    IntComplex int_div = intComplex_num1 / intComplex_num2;
    FloatComplex float_div = floatComplex_num1 / floatComplex_num2;
    cout << "Division of IntComplex numbers: " << int_div.getReal() << (int_div.getImaginary() >= 0 ? " + " : " - ") << abs(int_div.getImaginary()) << "i" << endl;
    cout << "Division of FloatComplex numbers: " << float_div.getReal() << (float_div.getImaginary() >= 0 ? " + " : " - ") << abs(float_div.getImaginary()) << "i" << endl;
}
