#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LABELS 10

void displayFile(char *filename, unsigned int *label_addresses, char *labels[]);
char *int_to_binary(int num, int bits);
int registerTokenToInt(char *token);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s filename\n", argv[0]);
        return 1;
    }

    printf("Assembly Language Program:\n");
    // array to store labels and their addresses
    unsigned int label_addresses[MAX_LABELS];
    char *labels[MAX_LABELS];

    // init label arrays
    for (int i = 0; i < MAX_LABELS; i++)
    {
        label_addresses[i] = 0;
        labels[i] = NULL;
    }
    displayFile(argv[1], label_addresses, labels);

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Couldn't open file\n");
        return 1;
    }

    // starting instruction address
    unsigned int address = 0x00400000;
    unsigned int globalAddress = 0x00400000;
    int opcode, rs, rt, rd, imm, shamt, funct;
    bool isIFormat, isRFormat, isJFormat, isException;

    printf("\n\nMachine Code:\n");

    char line[256];
    while (fgets(line, sizeof(line), fp))
    {
        globalAddress += 4;
        char *command = strdup(line);

        // check if the line is a label
        if (line[strlen(line) - 2] == ':')
        {
            continue;
        }

        isIFormat = false;
        isRFormat = false;
        isJFormat = false;
        isException = false;

        // tokenize string
        char *token = strtok(line, " ,$()");
        while (token != NULL)
        {
            // print address
            printf("0x%08X", address);

            if (strcmp(token, "addi") == 0)
            {
                opcode = 8;
                isIFormat = true;
            }
            else if (strcmp(token, "andi") == 0)
            {
                opcode = 12;
                isIFormat = true;
            }
            else if (strcmp(token, "ori") == 0)
            {
                opcode = 13;
                isIFormat = true;
            }
            else if (strcmp(token, "sw") == 0)
            {
                opcode = 43;
                rt = registerTokenToInt(strtok(NULL, " ,$"));

                char *imm_token = strtok(NULL, " ,$");
                if (imm_token == NULL)
                {
                    imm = 0;
                }
                else
                {
                    imm = atoi(imm_token);
                }

                rs = registerTokenToInt(strtok(NULL, " ,$"));
                isIFormat = true;
                isException = true;
            }
            else if (strcmp(token, "lw") == 0)
            {
                opcode = 35;
                rt = registerTokenToInt(strtok(NULL, " ,$"));

                char *imm_token = strtok(NULL, " ,$");
                if (imm_token == NULL)
                {
                    imm = 0;
                }
                else
                {
                    imm = atoi(imm_token);
                }

                rs = registerTokenToInt(strtok(NULL, " ,$"));
                isIFormat = true;
                isException = true;
            }
            else if (strcmp(token, "add") == 0)
            {
                funct = 32;
                isRFormat = true;
            }
            else if (strcmp(token, "sub") == 0)
            {
                funct = 34;
                isRFormat = true;
            }
            else if (strcmp(token, "and") == 0)
            {
                funct = 36;
                isRFormat = true;
            }
            else if (strcmp(token, "or") == 0)
            {
                funct = 37;
                isRFormat = true;
            }
            else if (strcmp(token, "xor") == 0)
            {
                funct = 38;
                isRFormat = true;
            }
            else if (strcmp(token, "slt") == 0)
            {
                funct = 42;
                isRFormat = true;
            }
            else if (strcmp(token, "beq") == 0)
            {
                opcode = 4;
                rs = registerTokenToInt(strtok(NULL, " ,$("));
                rt = registerTokenToInt(strtok(NULL, " ,$("));

                char *label = strtok(NULL, " ,$(");
                // remove trailing newline character if present
                if (label[strlen(label) - 1] == '\n')
                {
                    label[strlen(label) - 1] = '\0';
                }

                // search for label in array
                for (int i = 0; i < MAX_LABELS; i++)
                {
                    if (labels[i] != NULL && strcmp(labels[i], label) == 0)
                    {
                        imm = (label_addresses[i] - globalAddress) / 4;
                        break;
                    }
                }

                isIFormat = true;
                isException = true;
            }
            else if (strcmp(token, "j") == 0)
            {
                opcode = 2;

                char *label = strtok(NULL, " ,$");
                // remove trailing newline character if present
                if (label[strlen(label) - 1] == '\n')
                {
                    label[strlen(label) - 1] = '\0';
                }

                // search for label in array
                for (int i = 0; i < MAX_LABELS; i++)
                {
                    if (labels[i] != NULL)
                    {
                        if (strcmp(labels[i], label) == 0)
                        {
                            imm = label_addresses[i] >> 2;
                            break;
                        }
                    }
                }

                isJFormat = true;
            }

            if (isIFormat)
            {
                if (!isException)
                {
                    rt = registerTokenToInt(strtok(NULL, " ,$("));
                    rs = registerTokenToInt(strtok(NULL, " ,$("));
                    imm = atoi(strtok(NULL, " ,$("));
                }

                char *opcode_bin = int_to_binary(opcode, 6);
                char *rt_bin = int_to_binary(rt, 5);
                char *rs_bin = int_to_binary(rs, 5);
                char *imm_bin = int_to_binary(imm, 16);

                // I - format instruction concatenation
                char binary_str[33]; // 32 + 1 for null terminator
                sprintf(binary_str, "%s%s%s%s", opcode_bin, rs_bin, rt_bin, imm_bin);

                // convert binary string to hexadecimal
                unsigned int hex_value = strtol(binary_str, NULL, 2);
                printf("\t0x%08X", hex_value);

                rt, rs, imm = 0;
                free(opcode_bin);
                free(rt_bin);
                free(rs_bin);
                free(imm_bin);
            }
            else if (isRFormat)
            {
                opcode = 0;
                rd = registerTokenToInt(strtok(NULL, " ,$("));
                rs = registerTokenToInt(strtok(NULL, " ,$("));
                rt = registerTokenToInt(strtok(NULL, " ,$("));
                shamt = 0;

                char *opcode_bin = int_to_binary(opcode, 6);
                char *rs_bin = int_to_binary(rs, 5);
                char *rt_bin = int_to_binary(rt, 5);
                char *rd_bin = int_to_binary(rd, 5);
                char *shamt_bin = int_to_binary(shamt, 5);
                char *funct_bin = int_to_binary(funct, 6);

                // R - format instruction
                char binary_str[33];
                sprintf(binary_str, "%s%s%s%s%s%s", opcode_bin, rs_bin, rt_bin, rd_bin, shamt_bin, funct_bin);

                unsigned int hex_value = strtol(binary_str, NULL, 2);
                printf("\t0x%08X", hex_value);

                rt, rs, rd = 0;
                free(opcode_bin);
                free(rs_bin);
                free(rt_bin);
                free(rd_bin);
                free(shamt_bin);
                free(funct_bin);
            }
            else if (isJFormat)
            {
                char *opcode_bin = int_to_binary(opcode, 6);
                char *imm_bin = int_to_binary(imm, 26);
                char binary_str[33];
                sprintf(binary_str, "%s%s", opcode_bin, imm_bin);

                unsigned int hex_value = strtol(binary_str, NULL, 2);
                printf("\t0x%08X", hex_value);

                imm = 0;
                free(opcode_bin);
                free(imm_bin);
            }

            printf("\t%s", command);
            token = strtok(NULL, " ,$()");
        }

        free(command);
        printf("\n");
        address += 4;
    }

    fclose(fp);
    return 0;
}

void displayFile(char *filename, unsigned int *label_addresses, char *labels[])
{
    FILE *fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("Couldn't open file\n");
        exit(1);
    }

    char line[256];
    unsigned int address = 0x00400000;
    while (fgets(line, sizeof(line), fp))
    {
        printf("%s", line);

        char *token = strtok(line, " ,$()");

        // check if the line is a label
        if (token != NULL && token[strlen(token) - 2] == ':')
        {
            // remove ':' from label
            token[strlen(token) - 2] = '\0';
            // add label to arrays
            for (int i = 0; i < MAX_LABELS; i++)
            {
                if (labels[i] == NULL)
                {
                    labels[i] = strdup(token);
                    label_addresses[i] = address;
                    break;
                }
            }
        }

        address += 4;
    }

    fclose(fp);
}

char *int_to_binary(int num, int bits)
{
    // allocate memory for the binary string
    char *binary = (char *)malloc((bits + 1) * sizeof(char)); // + 1 for null terminator

    if (binary == NULL)
    {
        printf("Memory allocation failed\n");
        exit(1);
    }

    binary[bits] = '\0';

    // int to binary string
    for (int i = bits - 1; i >= 0; i--)
    {
        binary[i] = (num & 1) ? '1' : '0';
        num >>= 1;
    }

    return binary;
}

int registerTokenToInt(char *token)
{
    if (strncmp(token, "zero", 4) == 0) return 0;
    if (strncmp(token, "v0", 2) == 0) return 2;
    if (strncmp(token, "v1", 2) == 0) return 3;
    if (strncmp(token, "a0", 2) == 0) return 4;
    if (strncmp(token, "a1", 2) == 0) return 5;
    if (strncmp(token, "a2", 2) == 0) return 6;
    if (strncmp(token, "a3", 2) == 0) return 7;
    if (strncmp(token, "t0", 2) == 0) return 8;
    if (strncmp(token, "t1", 2) == 0) return 9;
    if (strncmp(token, "t2", 2) == 0) return 10;
    if (strncmp(token, "t3", 2) == 0) return 11;
    if (strncmp(token, "t4", 2) == 0) return 12;
    if (strncmp(token, "t5", 2) == 0) return 13;
    if (strncmp(token, "t6", 2) == 0) return 14;
    if (strncmp(token, "t7", 2) == 0) return 15;
    if (strncmp(token, "s0", 2) == 0) return 16;
    if (strncmp(token, "s1", 2) == 0) return 17;
    if (strncmp(token, "s2", 2) == 0) return 18;
    if (strncmp(token, "s3", 2) == 0) return 19;
    if (strncmp(token, "s4", 2) == 0) return 20;
    if (strncmp(token, "s5", 2) == 0) return 21;
    if (strncmp(token, "s6", 2) == 0) return 22;
    if (strncmp(token, "s7", 2) == 0) return 23;
    if (strncmp(token, "t8", 2) == 0) return 24;
    if (strncmp(token, "t9", 2) == 0) return 25;
    if (strncmp(token, "gp", 2) == 0) return 28;
    if (strncmp(token, "sp", 2) == 0) return 29;
    if (strncmp(token, "fp", 2) == 0) return 30;
    if (strncmp(token, "ra", 2) == 0) return 31;

    // return as it is if it's an int
    return atoi(token);
}
