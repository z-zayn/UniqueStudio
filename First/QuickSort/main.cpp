#include <stdio.h>

void quickSort(int a[], int head, int tail,int n)   // aΪ���������飬head��tailָ����a�����ݽ��п��ŵķ�Χ��n����������ĳ��������ж�Խ��
{
    int temp;
    int sentinel;
    sentinel=a[head];   // ָ���ڱ�
    int low=head;
    int high=tail;

    if(low >= high||low<0||high>n)  // �ݹ����
        return;

    while(low<high) // һ�˿��ŵ�����
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
    quickSort(a, head, low-1, n);   // �����ڱ�Ԫ��λ����������
    quickSort(a, low+1, tail, n);   // �Ҳ�
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
