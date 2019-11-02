#include <stdio.h>
int main()
{
    int a[100]={0};
    int n;
    int x;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
        scanf("%d",&x);
        a[x]++;
    }

    for (int i=0; i<100; i++)
    {
        if(a[i])
        {
            for(int j=1;j<=a[i];j++)
                printf("%d ",i);
        }
    }
    return 0;
}
