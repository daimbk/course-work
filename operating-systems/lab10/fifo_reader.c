#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <ctype.h>

#define FIFO_NAME "/tmp/myfifo"

int main()
{
    // open the named pipe (FIFO) for reading
    int fifo_fd = open(FIFO_NAME, O_RDONLY);

    if (fifo_fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // read a message from the other program
    char buffer[50];
    read(fifo_fd, buffer, sizeof(buffer));

    // convert the message to uppercase
    for (int i = 0; buffer[i]; ++i)
    {
        buffer[i] = toupper(buffer[i]);
    }

    // close the FIFO
    close(fifo_fd);

    // Open the FIFO for writing
    fifo_fd = open(FIFO_NAME, O_WRONLY);

    if (fifo_fd == -1)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    // send the uppercase message back to the writer
    write(fifo_fd, buffer, sizeof(buffer));

    // close the FIFO
    close(fifo_fd);

    return 0;
}
