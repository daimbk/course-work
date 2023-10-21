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

    fd = shm_open(name, O_RDWR, 0666);
    ptr = (char *)mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    exit_flag = (int *)(ptr + SIZE - sizeof(int));

    while (1)
    {
        if (*exit_flag == 1)
        {
            break;
        }

        printf("%s\n", (char *)ptr);
        sleep(1);
    }

    return 0;
}
