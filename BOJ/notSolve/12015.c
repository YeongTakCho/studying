#include <stdio.h>
#define MAXNUM 1000000
int main()
{
    int A;
    int Ai[MAXNUM];
    int data[MAXNUM] = {
        0,
    };
    int maxDataIndex = 0;
    scanf("%d", &A);
    for (int i = 0; i < A; i++)
    {
        scanf("%d", &Ai[i]);
    }

    for (int i = 0; i < A; i++)
    {
        int n = Ai[i];
        if (n > data[maxDataIndex])
        {
            maxDataIndex += 1;
            data[maxDataIndex] = n;
        }
        else
        {
            for (int j = 1; j <= maxDataIndex; j++)
            {
                if (n <= data[j])
                {
                    data[j] = n;
                    break;
                }
            }
        }
    }
    printf("%d\n", maxDataIndex);
}