#include <stdio.h>
#include <string.h>
#define S1_MAX_LEN 1000000
#define S2_MAX_LEN 36

int getNextS(int s1Len, int *isNotS, int start)
{
    for (int i = start; i < s1Len; i++)
    {
        if (isNotS[i] == 0)
        {
            return i;
        }
    }
    return -1;
}
int main()
{
    char s1[S1_MAX_LEN] = "12ab112ab2ab";
    int isNotS1[S1_MAX_LEN] = {0}; // value=0 -> not deleted, value=1 -> deleted
    char s2[S2_MAX_LEN] = "12ab";
    int cp_S2[S2_MAX_LEN] = {0};
    // scanf("%s", s1);
    // scanf("%s", s2);
    int s1Len = strlen(s1);
    int s2Len = strlen(s2);

    while (1)
    {
        int p = -1;
        int sameNum = 0;

        for (int i = 0; i <= s1Len - s2Len; i++)
        {
            p = getNextS(s1Len, isNotS1, p + 1);
            if (s1[p] == s2[0])
            {
                cp_S2[0] = p;
                int isSame = 0;
                for (int j = 1; j < s2Len; j++)
                {
                    p = getNextS(s1Len, isNotS1, p + 1);
                    if (s1[p] != s2[j])
                    {
                        break;
                    }
                    if (j == s2Len - 1)
                        isSame = 1;
                    cp_S2[j] = p;
                }

                if (isSame)
                {
                    sameNum += 1;
                    i += (s2Len - 1);
                    for (int pi = 0; pi < s2Len; pi++)
                    {
                        isNotS1[cp_S2[pi]] = 1;
                    }
                }
            }
        }
        if (sameNum == 0)
            break;
        printf("sameNum= %d\n", sameNum);
        s1Len -= (s2Len * sameNum);
    }

    if (s1Len > 0)
    {
        char ns1[S1_MAX_LEN];
        int p = -1;
        for (int i = 0; i < s1Len; i++)
        {
            p = getNextS(s1Len, isNotS1, p + 1);
            ns1[i] = s1[p];
        }
        printf("%s", ns1);
    }
    else
    {
        printf("FRULA");
    }

    return 0;
}