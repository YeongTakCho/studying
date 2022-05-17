#include <stdio.h>
#include <string.h>
#define MAX_LEN 1001

int findC(char c, char *s, int start, int sLen)
{
    for (int i = start; i < sLen; i++)
    {
        if (s[i] == c)
        {
            return i;
        }
    }
    return -1;
}

int LCS(char *s1, char *s2, int s1Len, int s2Len)
{
    int maxLen = 0;
    int db[MAX_LEN] = {-1};

    for (int i = 0; i < s1Len; i++)
    {
        char c = s1[i];
        for (int j = maxLen; j >= 0; j--)
        {
            int fc = findC(c, s2, db[j] + 1, s2Len);
            if (fc >= 0)
            {
                if (j == maxLen)
                {
                    db[j + 1] = fc;
                    maxLen += 1;
                }
                else
                {
                    if (fc < db[j + 1])
                    {
                        db[j + 1] = fc;
                    }
                }
            }
        }
    }
    return maxLen;
}

int main()
{
    int ans;
    char s1[MAX_LEN];
    char s2[MAX_LEN];
    scanf("%s", s1);
    scanf("%s", s2);
    int s1Len = strlen(s1);
    int s2Len = strlen(s2);
    if (s1Len <= s2Len)
    {
        ans = LCS(s1, s2, s1Len, s2Len);
    }
    else
        ans = LCS(s2, s1, s2Len, s1Len);
    printf("%d", ans);
    return 0;
}