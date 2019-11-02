#include <stdio.h>
void my_swap(int*,int,int);
void _merge(int*,int*,int,int,int);

void mergeSort(int a[], int b[], int head, int tail)
{
    int mid = (head+tail)/2;
    if(head == tail)  return;
    mergeSort(a, b, head, mid);
    mergeSort(a, b, mid+1, tail);
    _merge(a, b, head, mid, tail);
}

void _merge(int a[],int b[],int head,int mid,int tail)
{
    int i=head;
    int j=mid+1;
    int k=head;
    while(i<=mid&&j<=tail)
    {
        if(a[i]<=a[j])
            b[k++]=a[i++];
        else
            b[k++]=a[j++];
    }
    while(i<=mid)
        b[k++]=a[i++];
    while(j<=tail)
        b[k++]=a[j++];
    for(int i=head;i<=tail;i++)
        a[i]=b[i];
}

void my_swap(int a[],int i, int j)  // 数组内部的数据交换
{
    int temp;
    temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void print_arr(int *a, int n)
{
    int i;
    for (i=0; i<n; i++)
    {
        if (i == n - 1)
            printf("%d\n", a[i]);
        else
            printf("%d ", a[i]);
    }
}

int main()
{
    int a[100]={0};
    int b[100]={0};
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
        scanf("%d",&a[i]);

    mergeSort(a, b, 0, n-1);

    print_arr(a, n);
    return 0;
}
