#include<stdio.h>
void quicksort(int arr[50],int start,int end){
   int i, j, pivot, temp;

   if(start<end){
      pivot=start;
      i=start;
      j=end;

      while(i<j){
         while(arr[i]<=arr[pivot])
            i++;
         while(arr[j]>arr[pivot])
            j--;
         if(i<j){
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
         }
      }

      temp=arr[pivot];
      arr[pivot]=arr[j];
      arr[j]=temp;
      quicksort(arr,start,j-1);
      quicksort(arr,j+1,end);

   }
}

int main(){
   int i, n, arr[50];

   printf("enter no.of elements to be stored in the array:");
   scanf("%d",&n);

   printf("Enter %d elements: ", n);
   for(i=0;i<n;i++)
      scanf("%d",&arr[i]);

   quicksort(arr,0,n-1);

   printf("required sorted elements are: ");
   for(i=0;i<n;i++)
      printf("%d ",arr[i]);

   return 0;
}
