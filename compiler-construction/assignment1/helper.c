#include "helper.h"

void copyString(char *dest, const char *src) {
    while (*src) {
        *dest = *src;
        src++;
        dest++;
    }

    *dest = '\0'; // Null-terminate
}

int stringLength(const char *str) {
    // get len of string
    int length = 0;
    while (*str) {
        length++;
        str++;
    }

    return length;
}

void stringScanf(const char *input, const char *format, char *output1, char *output2) {
    while (*format) {
        if (*format == '%') {
            switch (*(++format)) {
                case 's':
                    while (*input && *input != ' ') {
                        *output1++ = *input++;
                    }
                    *output1 = '\0'; // Null-terminate output
                    break;
                case '[': // read until newline
                    while (*input && *input != '\n') {
                        *output2++ = *input++;
                    }
                    *output2 = '\0';
                    break;
            }
        } else {
            if (*input != *format) {
                break;
            }

            input++;
        }

        format++;
    }
}
