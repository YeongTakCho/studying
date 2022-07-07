#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
    int fd1, fd2;
    char c;
    char name[10] = "test.txt";
    fd1 = open(name, O_RDONLY);
    fd2 = open(name, O_RDONLY);
    read(fd2, &c, 1);
    read(fd1, &c, 1);
    printf("c = %c\n", c);
    return 0;
}