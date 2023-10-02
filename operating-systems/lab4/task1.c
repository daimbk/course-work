#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>


int main(int argc, char *argv[])
{
    if (argc < 3) {
        printf("Usage: task1 {number of child processes} {number of grand-child processes}");
        return (-1);
    }

    int child_processes = atoi(argv[1]);
    int grand_children = atoi(argv[2]);

    pid_t pid1, pid2;

    for (int i = 0; i < child_processes; i++) {
        pid1 = fork();
        
        if (pid1 > 0 ) {
            printf("Parent: My pid = %d\n", getpid());
            printf("Parent: My parent's pid = %d\n", getppid());
            printf("Parent: My child's pid = %d\n", pid1);
        }

        else if (pid1 == 0) {

            printf("Child: My pid = %d\n", getpid());
            printf("Child: My parent's pid = %d\n", getppid());

            pid2 = fork();
            for (int j = 0; j < grand_children; j++) {
                if (pid2 == 0) {
                    printf("Grand Child: My pid = %d\n", getpid());
                    printf("Grand Child: My parent's pid = %d\n", getppid());
                }

                else if (pid2 > 0) {
                    wait(NULL);
                }
            }
        }
    }

    return 0;
}
