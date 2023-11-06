#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *messagePrinter(void *arg);

int main()
{
    pthread_t tid1, tid2, tid3;

    char message1[] = "a";
    char message2[] = "b";
    char message3[] = "c";

    printf("Threads Starting\n");
    pthread_create(&tid1, NULL, messagePrinter, (void *)message1);
    pthread_create(&tid2, NULL, messagePrinter, (void *)message2);
    pthread_create(&tid3, NULL, messagePrinter, (void *)message3);

    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);
    pthread_join(tid3, NULL);
    return 0;
}

void *messagePrinter(void *arg)
{
    pthread_t tid = pthread_self();
    char *message = (char *)arg;

    printf("Thread %ld: %s\n", tid, message);

    pthread_exit(0);
}
