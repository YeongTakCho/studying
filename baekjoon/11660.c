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

    for (int i = 1; i < N; i++)
    {
        graph[0][i] += graph[0][i - 1];
        graph[i][0] += graph[i - 1][0];
    }

    for (int i = 1; i < N; i++)
    {
        for (int j = 1; j < N; j++)
        {
            graph[i][j] += graph[i - 1][j];
            graph[i][j] += graph[i][j - 1];
            graph[i][j] -= graph[i - 1][j - 1];
        }
    }

    for (int i = 0; i < M; i++)
    {
        v = 0;
        scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
        x0 -= 1;
        x1 -= 1;
        y0 -= 1;
        y1 -= 1;
        v = graph[x1][y1];
        if (x0 > 0 && y0 > 0)
            v += graph[x0 - 1][y0 - 1];
        if (y0 > 0)
            v -= graph[x1][y0 - 1];
        if (x0 > 0)
            v -= graph[x0 - 1][y1];
        printf("%d\n", v);
    }
}