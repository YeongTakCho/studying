#include <stdio.h>
#define MAXSIZE 1024

int main()
{
    int N, M;
    int x0, y0, x1, y1;
    int graph[MAXSIZE][MAXSIZE];
    int v;

    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &graph[i][j]);
        }
    }

    for (int i = 0; i < M; i++)
    {
        v = 0;
        scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
        for (int yp = y0 - 1; yp <= y1 - 1; yp++)
        {
            for (int xp = x0 - 1; xp <= x1 - 1; xp++)
            {
                v += graph[xp][yp];
            }
        }
        printf("%d\n", v);
    }
}