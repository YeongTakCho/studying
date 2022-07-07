#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
int main()
{
    char buffer[] = {"1345"};
    char line_change[] = {"\n"};
    int output_fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 777);
    lseek(output_fd, 0, SEEK_END);
    write(output_fd, buffer, strlen(buffer));
    write(output_fd, line_change, 1);
    write(output_fd, buffer, strlen(buffer));
    write(output_fd, buffer, strlen(buffer));
    printf("%ld", strlen(buffer));
}