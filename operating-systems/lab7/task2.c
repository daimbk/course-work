#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *factorial(void *arg);

int main()
{
    pthread_t tid1, tid2, tid3, compileThread;
    void *n_factorial, *r_factorial, *n_minus_r_factorial;

    int n = 4, r = 3;
    int n_minus_r = n - r;

    printf("Threads Starting\n");
    pthread_create(&tid1, NULL, factorial, &n);
    pthread_create(&tid2, NULL, factorial, &r);
    pthread_create(&tid3, NULL, factorial, &n_minus_r);

    pthread_join(tid1, &n_factorial);
    pthread_join(tid2, &r_factorial);
    pthread_join(tid3, &n_minus_r_factorial);

    int result = (__intptr_t)n_factorial / ((__intptr_t)r_factorial * (__intptr_t)n_minus_r_factorial);
    printf("Result: %d\n", result);

    return 0;
}

void *factorial(void *arg)
{
    int n = *(int *)arg;

    int fact = 1;

    for (int i = 1; i <= n; i++)
        fact = fact * i;

    printf("%d : %d\n", n, fact);

    return (void *)(__intptr_t)fact;
}
