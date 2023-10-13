#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int countWords(FILE *file, long startPosition, long endPosition)
{
    if (file == NULL)
    {
        fprintf(stderr, "Invalid file pointer\n");
        return -1;
    }

    int wordCount = 0;
    char word[256];
    bool inChunk = false;

    fseek(file, startPosition, SEEK_SET);
    while (ftell(file) < endPosition && fscanf(file, "%255s", word) != EOF)
    {
        wordCount++;
        inChunk = true;
    }

    if (inChunk && ftell(file) > endPosition)
    {
        wordCount--;
    }

    return wordCount;
}

int main()
{
    char filename[256];
    printf("Enter filename: ");
    scanf("%255s", filename);

    FILE *file;
    file = fopen(filename, "r");
    if (file == NULL)
    {
        perror("fopen");
        return 1;
    }

    // get total file size
    fseek(file, 0, SEEK_END);
    long fileSize = ftell(file);
    fseek(file, 0, SEEK_SET);

    int numChunks;
    printf("Enter the number of chunks to divide the file into: ");
    scanf("%d", &numChunks);

    if (numChunks <= 0)
    {
        printf("Invalid number of chunks\n");
        fclose(file);
        return 1;
    }

    // divide the file into chunks
    long chunkSize = fileSize / numChunks;
    long startPosition = 0;

    int totalWordCount = 0;

    for (int i = 0; i < numChunks; i++)
    {
        long endPosition = startPosition + chunkSize;

        if (i == numChunks - 1)
        {
            // check for last chunk if its smaller
            endPosition = fileSize;
        }

        // fork a child process
        pid_t child_pid = fork();

        if (child_pid == 0)
        {
            // child process calls func
            int wordCount = countWords(file, startPosition, endPosition);
            exit(wordCount);
        }
        else if (child_pid < 0)
        {
            perror("fork");
        }
        else
        {
            // wait for child process to finish
            int status;
            waitpid(child_pid, &status, 0);

            if (WIFEXITED(status))
            {
                totalWordCount += WEXITSTATUS(status);
                printf("Chunk %d: Number of words: %d\n", i + 1, WEXITSTATUS(status));
            }
        }

        // set next chunk's starting position
        startPosition = endPosition;
    }

    printf("Total word count: %d\n", totalWordCount);

    fclose(file);
    return 0;
}
