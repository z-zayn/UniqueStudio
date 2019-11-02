#include <stdio.h>

void insertSort(int a[],int n){
    int i,j,low,high,mid,temp;
    for(i=1;i<n;i++){
        temp=a[i];
        low=0;
        high=i-1;   // 设置折半查找的范围,从0到i-1,temp用来暂存元素
        while(low<=high){
            mid=(low+high)/2;
            if(a[mid]>temp)
                high=mid-1; // 查找左半子表
            else
                low=mid+1; // 查找右半子表
        }

        for(j=i-1;j>=high+1;--j)
                a[j+1]=a[j];    // 统一向后移动元素，空出插入位置
        a[high+1]=temp; // 插入操作
    }
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

    insertSort(a, n);

    print_arr(a, n);
    return 0;
}
