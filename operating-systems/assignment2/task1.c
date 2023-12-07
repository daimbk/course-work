/*
COMP 301 - B
Assignment 2
07/12/23
Daim Bin Khalid
251686775
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATH_LEN 256

void processInfo(char *pid)
{
    // file paths
    char status_path[MAX_PATH_LEN];
    char cmdline_path[MAX_PATH_LEN];
    char fd_path[MAX_PATH_LEN];

    snprintf(status_path, MAX_PATH_LEN, "/proc/%s/status", pid);
    snprintf(cmdline_path, MAX_PATH_LEN, "/proc/%s/cmdline", pid);
    snprintf(fd_path, MAX_PATH_LEN, "/proc/%s/fd", pid);

    // display process ID
    printf("Process ID (PID): %s\n", pid);

    // read and display parent process ID
    char parent_pid[MAX_PATH_LEN];
    FILE *status_file = fopen(status_path, "r");
    if (status_file != NULL)
    {
        while (fscanf(status_file, "PPid:\t%s", parent_pid) != 1)
            ;
        fclose(status_file);
        printf("Parent Process ID (PPID): %s\n", parent_pid);
    }

    // read and display command line
    char cmdline[MAX_PATH_LEN];
    FILE *cmdline_file = fopen(cmdline_path, "r");
    if (cmdline_file != NULL)
    {
        fread(cmdline, 1, sizeof(cmdline), cmdline_file);
        fclose(cmdline_file);
        printf("Command Line: %s\n", cmdline);
    }

    // display memory utilization information from the status file
    printf("Memory Utilization Information:\n");
    system("cat /proc/$$/status | grep -E 'VmSize|VmRSS'");

    // display list of open files from the fd directory
    printf("List of Open Files:\n");
    system("ls -l /proc/$$/fd");
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <PID>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    processInfo(argv[1]);

    return 0;
}
