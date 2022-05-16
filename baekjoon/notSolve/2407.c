// 엄청 큰 수에 대한 표현을 구현해야 됨
#include <stdio.h>

int main()
{
    int n, m;
    unsigned long v = 1;
    scanf("%d %d", &n, &m);
    if (m * 2 > n)
    {
        m = n - m;
    }

    for (int i = 1; i <= m; i++)
    {
        v *= (n - i + 1);
        v /= i;
    }
    printf("%ld", v);
    return 0;
}