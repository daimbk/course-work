#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define FIFO_NAME "/tmp/myfifo"

int main()
{
    // create the named pipe (FIFO) if it doesn't exist
    mkfifo(FIFO_NAME, 0666);

    int fifo_fd = open(FIFO_NAME, O_WRONLY);

    if (fifo_fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // send a message to the other program
    char message[] = "lowercase message from program 1!";
    write(fifo_fd, message, sizeof(message));

    // close the FIFO
    close(fifo_fd);

    // open the named pipe (FIFO) for reading
    fifo_fd = open(FIFO_NAME, O_RDONLY);

    if (fifo_fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // read a message from the other program
    char buffer[50];
    read(fifo_fd, buffer, sizeof(buffer));
    printf("%s\n", buffer);

    // close the FIFO
    close(fifo_fd);

    // remove the named pipe (FIFO)
    unlink(FIFO_NAME);

    return 0;
}
