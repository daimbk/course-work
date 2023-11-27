#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#define N 6

int A[N][N], B[N][N];
pthread_mutex_t mutex;
FILE *file;

void *calculate_matrix(void *arg);

int main()
{
    pthread_t tid[6];
    pthread_mutex_init(&mutex, NULL);

    file = fopen("result.txt", "w");

    for (int k = 0; k < 6; ++k)
    {
        pthread_create(&tid[k], NULL, calculate_matrix, (void *)(intptr_t)k + 1);
    }

    for (int k = 0; k < 6; ++k)
    {
        pthread_join(tid[k], NULL);
    }

    fclose(file);
    pthread_mutex_destroy(&mutex);

    printf("Matrices result stored in file\n");

    return 0;
}

void *calculate_matrix(void *arg)
{
    int k = (intptr_t)arg;

    pthread_mutex_lock(&mutex);
    fprintf(file, "\nMatrix %d:\n", k);
    pthread_mutex_unlock(&mutex);

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            A[i][j] = (3 * (pow(i, k))) - (2 * (pow(j, k)));
            pthread_mutex_lock(&mutex);
            fprintf(file, "%d ", A[i][j]);
            pthread_mutex_unlock(&mutex);
        }
        pthread_mutex_lock(&mutex);
        fprintf(file, "\n");
        pthread_mutex_unlock(&mutex);
    }

    pthread_exit(NULL);
}
