#include <stdio.h>
#include <string.h>
#define S1_MAX_LEN 1000000
#define S2_MAX_LEN 36

int main()
{
    char s1[S1_MAX_LEN];
    char s2[S2_MAX_LEN];
    scanf("%s", s1);
    scanf("%s", s2);
    int s1Len = strlen(s1);
    int s2Len = strlen(s2);
    while (1)
    {
        int sameNum = 0;
        int sameI[S1_MAX_LEN] = {0};
        for (int i = 0; i <= s1Len - s2Len; i++)
        {
            if (s1[i] == s2[0])
            {
                int isSame = 0;
                for (int j = 1; j < s2Len; j++)
                {
                    if (s1[i + j] != s2[j])
                    {
                        break;
                    }
                    if (j == s2Len - 1)
                        isSame = 1;
                }

                if (isSame)
                {
                    sameI[sameNum] = i;
                    sameNum += 1;
                    i += (s2Len - 1);
                }
            }
        }
        if (sameNum == 0)
            break;

        sameI[sameNum] = s1Len;
        for (int i = 0; i < sameNum; i++)
        {
            for (int p = sameI[i] + s2Len; p < sameI[i + 1]; p++)
            {
                s1[p - (i + 1) * s2Len] = s1[p];
            }
        }
        s1Len -= (s2Len * sameNum);
    }

    if (s1Len > 0)
    {
        char ns1[S1_MAX_LEN];
        for (int i = 0; i < s1Len; i++)
        {
            ns1[i] = s1[i];
        }
        printf("%s", ns1);
    }
    else
    {
        printf("FRULA");
    }

    return 0;
}