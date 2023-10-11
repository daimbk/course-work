#include <iostream>

void merge(int listA[], int start, int div1, int div2, int end)
{
    int listB[end - start + 1];

    int i = start;
    int j = div1;
    int k = div2;
    int l = 0;

    while ((i < div1) && (j < div2) && (k <= end))
    {
        if (listA[i] < listA[j])
        {
            if (listA[i] < listA[k])
            {
                listB[l++] = listA[i++];
            }
            else
            {
                listB[l++] = listA[k++];
            }
        }
        else
        {
            if (listA[j] < listA[k])
            {
                listB[l++] = listA[j++];
            }
            else
            {
                listB[l++] = listA[k++];
            }
        }
    }

    while (i < div1 && j < div2)
    {
        if (listA[i] < listA[j])
        {
            listB[l++] = listA[i++];
        }
        else
        {
            listB[l++] = listA[j++];
        }
    }

    while (j < div2 && k <= end)
    {
        if (listA[j] < listA[k])
        {
            listB[l++] = listA[j++];
        }
        else
        {
            listB[l++] = listA[k++];
        }
    }

    while (i < div1 && k <= end)
    {
        if (listA[i] < listA[k])
        {
            listB[l++] = listA[i++];
        }
        else
        {
            listB[l++] = listA[k++];
        }
    }

    while (i < div1)
        listB[l++] = listA[i++];

    while (j < div2)
        listB[l++] = listA[j++];

    while (k <= end)
        listB[l++] = listA[k++];

    for (i = start; i <= end; i++)
    {
        listA[i] = listB[i - start];
    }
}

void mergeSort(int listA[], int start, int end)
{
    if (start < end)
    {
        int div1 = start + (end - start) / 3;
        int div2 = start + 2 * (end - start) / 3;

        mergeSort(listA, start, div1);
        mergeSort(listA, div1 + 1, div2);
        mergeSort(listA, div2 + 1, end);
        merge(listA, start, div1, div2, end);
    }
}

int main()
{
    int listA[] = {2, 5, 8, 1, 3, 6};
    int size = sizeof(listA) / sizeof(listA[0]);

    std::cout << "Original array: ";
    for (int i = 0; i < size; i++)
    {
        std::cout << listA[i] << " ";
    }
    std::cout << std::endl;

    mergeSort(listA, 0, size - 1);

    std::cout << "Sorted array: ";
    for (int i = 0; i < size; i++)
    {
        std::cout << listA[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
