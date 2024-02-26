#ifndef VALIDATE_H
#define VALIDATE_H

void args_check(int argc);
int validate_number(char *argv[]);
void disp_file_on_console(FILE *file);
void file_decoder(FILE *file, int positions);

#endif
