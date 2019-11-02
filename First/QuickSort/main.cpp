#include <stdio.h>

void quickSort(int a[], int head, int tail,int n)   // a为待排序数组，head和tail指定对a中数据进行快排的范围，n是整个数组的长度用来判断越界
{
    int temp;
    int sentinel;
    sentinel=a[head];   // 指定哨兵
    int low=head;
    int high=tail;

    if(low >= high||low<0||high>n)  // 递归出口
        return;

    while(low<high) // 一趟快排的流程
    {
        while(low<high&&sentinel<=a[high])
        {
            high--;
        }
        a[low]=a[high];

        while(low<high&&sentinel>=a[low])
        {
            low++;
        }
        a[high]=a[low];

    }
    a[low]=sentinel;
    quickSort(a, head, low-1, n);   // 快排哨兵元素位置左侧的数据
    quickSort(a, low+1, tail, n);   // 右侧
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
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
        scanf("%d",&a[i]);

    quickSort(a, 0, n-1, n);

    print_arr(a, n);
    return 0;
}
