#include <stdio.h>
#define MAXSIZE 100001

int main()
{
    int testcase;
    int table[2][MAXSIZE] = {{0}};

    scanf("%d", &testcase);

    for (int tc = 0; tc < testcase; tc++)
    {
        int width;
        scanf("%d", &width);
        for (int i = 0; i < 2; i++) // input arr
        {
            table[i][0] = 0;
            for (int j = 1; j <= width; j++)
                scanf("%d", &table[i][j]);
        }
        // use dp
        for (int i = 2; i <= width; i++)
        {
            table[0][i] += (table[1][i - 2] > table[1][i - 1] ? table[1][i - 2] : table[1][i - 1]);
            table[1][i] += (table[0][i - 2] > table[0][i - 1] ? table[0][i - 2] : table[0][i - 1]);
        }
        int ans0 = (table[0][width] > table[0][width - 1] ? table[0][width] : table[0][width - 1]);
        int ans1 = (table[1][width] > table[1][width - 1] ? table[1][width] : table[1][width - 1]);
        int ans = ans0 > ans1 ? ans0 : ans1;

        printf("%d\n", ans);
    }

    return 0;
}