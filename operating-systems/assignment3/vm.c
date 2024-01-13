/*
COMP 301 - B Operating Systems
Assignment 3

Daim Bin Khalid
251686775
13 Jan 2024
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int frameUsed = 0;

struct PageTableEntry
{
    int pageNumber;
    int frameNumber;
};

// func: init with specified number of entries
struct PageTableEntry *initPageTable(int numOfEntries)
{
    struct PageTableEntry *pageTable = (struct PageTableEntry *)malloc(numOfEntries * sizeof(struct PageTableEntry));

    // assign page number and frame number to each entry
    for (int i = 0; i < numOfEntries; i++)
    {
        pageTable[i].pageNumber = i;
        pageTable[i].frameNumber = -1;
    }

    return pageTable;
}

// func: simulate a page fault and load the missing page into memory with FIFO
void handlePageFault(struct PageTableEntry *pageTable, int numEntries, int virtualPageNumber, int *fifoQueue, int *fifoIndex)
{
    for (int i = 0; i < numEntries; i++)
    {
        if (pageTable[i].frameNumber == -1)
        {
            // assign virtual page to the available frame
            pageTable[i].pageNumber = virtualPageNumber;
            pageTable[i].frameNumber = frameUsed;
            frameUsed++;

            // update FIFO queue
            fifoQueue[*fifoIndex] = i;
            *fifoIndex = (*fifoIndex + 1) % numEntries;

            printf("Page Fault: Loading virtual page %d into physical frame %d\n", virtualPageNumber, i);
            return;
        }
    }

    // no available frames, perform page replacement using FIFO algorithm
    int replacedFrameIndex = fifoQueue[*fifoIndex];
    int replacedPageNumber = pageTable[replacedFrameIndex].pageNumber;

    // assign new virtual page to the frame
    pageTable[replacedFrameIndex].pageNumber = virtualPageNumber;

    fifoQueue[*fifoIndex] = replacedFrameIndex;
    *fifoIndex = (*fifoIndex + 1) % numEntries;

    printf("Page Fault: Loading virtual page %d into physical frame %d (Replacing page %d)\n", virtualPageNumber, replacedFrameIndex, replacedPageNumber);
}

// func: lookup a page table entry
struct PageTableEntry *pageTableLookup(struct PageTableEntry *pageTable, int numOfEntries, int virtualPageNumber)
{
    for (int i = 0; i < numOfEntries; i++)
    {
        if (pageTable[i].pageNumber == virtualPageNumber)
        {
            return &pageTable[i];
        }
    }

    return NULL;
}

void displayPageTable(struct PageTableEntry *pageTable, int numOfEntries)
{
    printf("Page Table:\n");
    for (int i = 0; i < numOfEntries; i++)
    {
        printf("Entry %d - Page: %d, Frame: %d\n", i + 1, pageTable[i].pageNumber, pageTable[i].frameNumber);
    }

    printf("\n");
}

int main()
{
    int numOfEntries = 10;
    struct PageTableEntry *pageTable = initPageTable(numOfEntries);

    printf("Initial Page Table:\n");
    displayPageTable(pageTable, numOfEntries);

    srand(time(NULL));

    // simulate random page accesses
    int numAccesses = 12;
    int fifoQueue[numOfEntries];
    int fifoIndex = 0;

    printf("FIFO Page Replacement Algorithm:\n");

    for (int i = 0; i < numAccesses; i++)
    {
        int virtualPageNumberToAccess = rand() % 100;

        // page table lookup
        struct PageTableEntry *result = pageTableLookup(pageTable, numOfEntries, virtualPageNumberToAccess);

        if (result != NULL)
        {
            // page is in memory
            printf("Access %d: Virtual page %d is in physical frame %d\n", i + 1, virtualPageNumberToAccess, result->frameNumber);
        }
        else
        {
            // page fault
            printf("Access %d: ", i + 1);
            handlePageFault(pageTable, numOfEntries, virtualPageNumberToAccess, fifoQueue, &fifoIndex);
        }

        // display page table after each access
        displayPageTable(pageTable, numOfEntries);
    }

    free(pageTable);
    return 0;
}
