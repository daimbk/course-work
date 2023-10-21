#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    const int SIZE = 4096;
    const char *name = "OS";
    int fd;
    char *ptr;
    int *exit_flag;

    fd = shm_open(name, O_CREAT | O_RDWR, 0666);

    ftruncate(fd, SIZE);
    ptr = (char *)mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    exit_flag = (int *)(ptr + SIZE - sizeof(int));

    while (1)
    {
        char message[100];
        scanf("%s", message);

        if (strcmp(message, "exit") == 0)
        {
            *exit_flag = 1;
            break;
        }
        else
        {
            message[strcspn(message, "\n")] = 0;
            strcpy(ptr, message);
        }
    }

    shm_unlink(name);
    return 0;
}
