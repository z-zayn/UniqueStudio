#include <stdio.h>

void bubbleSort(int a[], int n,bool way=true)
{
    int temp;
    for(int i=0; i<n-1; i++)
        for(int j=0; j<n-i-1; j++)
        {
            if(way)
            {
                if(a[j]>a[j+1])
                {
                    temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
            }
            else
            {
                if(a[j]<a[j+1])
                {
                    temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
            }
        }
}

void prin_arr(int *a, int n)   // Êä³öÊý×é
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
    int a[100];
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
        scanf("%d",&a[i]);

    bubbleSort(a, n);

    print_arr(a, n);
    return 0;
}
