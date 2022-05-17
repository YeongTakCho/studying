/* Solution code for "BOJ 11049. Çà·Ä °ö¼À ¼ø¼­".

- Problem link: https://www.acmicpc.net/problem/11049
- MY Solution link: https://www.acmicpc.net/source/43454670
- Solution link:
*/
#include <stdio.h>
#define INF 1000000000
#define MAXSIZE 501
int min(int a, int b)
{
    return a < b ? a : b;
}

int main()
{
    int N;
    int start, end, v;
    int d[MAXSIZE];
    int dp[MAXSIZE][MAXSIZE] = {0};

    scanf("%d", &N);
    scanf("%d %d", &d[0], &d[1]);
    for (int i = 0; i < N - 1; i++)
    {
        scanf("%d %d", &d[i + 1], &d[i + 2]);
    }
    for (int distance = 2; distance < N + 1; distance++)
    {
        for (int i = 0; i < N - distance + 1; i++)
        {
            start = i;
            end = i + distance;
            dp[start][end] = INF;
            for (int m = start + 1; m < end; m++)
            {
                v = dp[start][m] + dp[m][end] + d[start] * d[m] * d[end];
                if (v < dp[start][end])
                {
                    dp[start][end] = v;
                }
            }
        }
    }
    printf("%d\n", dp[0][N]);
}