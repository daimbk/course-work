/*
COMP 301 - B
Daim Bin Khalid
251686775
18/09/23
*/

#include <stdio.h>


int main()
{
	int List[30] = {22, 24, 25, 26, 21, 30, 11, 
			15, 16, 18, 20, 21, 24, 23, 
			21, 20, 26, 18, 29, 30, 28, 
			27, 25, 21, 26, 29, 25, 20, 
			19, 18};
	
	int week = 1, day_counter = 1;
	int temp = 0;
	for (int i = 0; i < 30; i++) {
		if (List[i] > temp) {
			temp = List[i];
		}
		
		if (day_counter % 7 == 0 || day_counter == 30) {
			printf("Week %d: %d\n", week, temp);
			week++;
			temp = 0;
		}
		
		day_counter++;
	}
}

