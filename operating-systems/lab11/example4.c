#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *arr = (int *)malloc(3 * sizeof(int));

    arr[3] = 42;

    free(arr);

    return 0;
}
