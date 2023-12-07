/*
COMP 301 - B
Assignment 2
07/12/23
Daim Bin Khalid
251686775
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#define MAX_PATH_LEN 256
#define MAX_BUFFER_LEN 1024

// read and display total and free memory
void displayMemoryInfo()
{
    FILE *memInfo = fopen("/proc/meminfo", "r");
    if (memInfo != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        while (fgets(buffer, sizeof(buffer), memInfo) != NULL)
        {
            if (strncmp(buffer, "MemTotal:", 9) == 0 || strncmp(buffer, "MemFree:", 8) == 0)
            {
                printf("%s", buffer);
            }
        }
        fclose(memInfo);
    }
    else
    {
        perror("Error opening /proc/meminfo");
    }
}

// read and display CPU usage
void displayCpuUsage()
{
    FILE *statFile = fopen("/proc/stat", "r");
    if (statFile != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        if (fgets(buffer, sizeof(buffer), statFile) != NULL)
        {
            if (strncmp(buffer, "cpu ", 4) == 0)
            {
                unsigned long long user, nice, system, idle;
                sscanf(buffer + 4, "%llu %llu %llu %llu", &user, &nice, &system, &idle);

                unsigned long long totalCpuTime = user + nice + system + idle;
                unsigned long long idleTime = idle;

                double cpuUsage = ((totalCpuTime - idleTime) * 100.0) / totalCpuTime;
                printf("CPU Usage: %.2f%%\n", cpuUsage);
            }
        }
        fclose(statFile);
    }
    else
    {
        perror("Error opening /proc/stat");
    }
}

// read and display disk usage
void displayDiskUsage()
{
    FILE *df = popen("df -h /", "r");
    if (df != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        if (fgets(buffer, sizeof(buffer), df) != NULL)
        {
            printf("Disk Usage: %s", buffer);
        }
        pclose(df);
    }
    else
    {
        perror("Error running df command");
    }
}

// display the top N processes
void displayTopProcesses(int topN)
{
    printf("Top %d Processes:\n", topN);

    // Run 'ps' command to get the top processes
    FILE *ps = popen("ps aux --sort=-%cpu,%mem | head -n+6", "r");
    if (ps != NULL)
    {
        char buffer[MAX_BUFFER_LEN];
        int counter = 1; // Counter for numbering processes
        while (fgets(buffer, sizeof(buffer), ps) != NULL)
        {
            printf("%-3d%s", counter++, buffer); // Display process number
        }
        pclose(ps);
    }
    else
    {
        perror("Error running ps command");
    }
}

int main()
{
    int updateInterval = 5; // seconds
    int topNProcesses = 5;

    while (1)
    {
        // clear the terminal
        system("clear");

        // display system information
        printf("System Information:\n");
        displayMemoryInfo();
        displayCpuUsage();
        displayDiskUsage();
        displayTopProcesses(topNProcesses);

        // sleep for the specified update interval
        sleep(updateInterval);
    }

    return 0;
}
