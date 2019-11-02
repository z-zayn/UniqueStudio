#include <stdio.h>

void initHeap(int*, int);
void MaxHeapify(int*, int, int);
void my_swap(int*, int ,int);

void initHeap(int a[],int n)    // 初始化第一个大顶堆
{
    for(int i=n/2;i>=0;i--)
        MaxHeapify(a, i, n);
}

void MaxHeapify(int a[],int i,int _size)  // 建立大顶堆
{
    int left = 2*i + 1;                     // 根据完全二叉树的节点关系
    int right = left + 1;
    int _max = i;
    if(left<_size && a[left]>a[_max])
        _max = left;
    if(right<_size && a[right]>a[_max])
        _max = right;
    if(_max != i)
    {
        my_swap(a, i, _max);
        MaxHeapify(a, _max, _size);
    }
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
    int n;
    int _size;
    scanf("%d", &n);
    _size = n;
    for(int i=0; i<n; i++)
        scanf("%d",&a[i]);

    initHeap(a, n);

    for(int i=n-1;i>=0;i--)
    {
        my_swap(a, 0, i);
        _size--;
        MaxHeapify(a, 0, _size);
    }

    print_arr(a, n);
    return 0;
}
