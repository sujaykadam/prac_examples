#include<stdio.h>

int ar[10]={9,5,2,6,10,4,8,1,3,7};

int swaper(int low, int high){
	
	int pivot, temp;
	int ind=high;
	pivot = ar[ind];
	high--;
	while(low<high){
		if (ar[low]<pivot)
		low++;
		if (ar[high]>pivot)
		high--;
		temp=ar[low];
		ar[low]=ar[high];
		ar[high]=temp;
		low++;
		high--;	
	}
	temp=ar[ind];
	ar[ind]=ar[low];
	ar[low]=temp;
	return low;
}

void quicksort(int low, int high){
	if(low<high){
		int sor = swaper(low, high);
		quicksort(low, sor-1);
		quicksort(sor+1, high);
	}
	else
	return;
}
void main() {
	
	int i;
	for(i=0;i<10;i++)
	printf("%d ",ar[i]);
	printf("\n");
	
	quicksort(0, 9);	
	
	for(i=0;i<10;i++)
	printf("%d ",ar[i]);
	
}
