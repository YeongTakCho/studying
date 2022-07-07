// command : ./ku_fs str i input output
// argc= 4, argv[0] = ./ku_fs, argv[1] = str, argv[2] = i, argv[3] = input, argv[4] = output
// str: substring to find
// i: number of parallel threads (>0)
// input: input file, output: output file
// example command: ./ku_fs OYA 12 sample_input.txt output.txt
// compile command: gcc -o ku_fs ku_fs.c

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <pthread.h>
#define STRLEN 6

int occupied_lines;
char *find_str;
int input_fd;

typedef struct
{
    int n;
    int index[1024];
} my_ret;

void *thread_routine(void *arg)
{
    char *buffer = malloc(sizeof(char) * 4096);
    int *i = (int *)arg;
    ssize_t ret_read;
    my_ret *ret = malloc(sizeof(my_ret));
    ret->n = 0;
    lseek(input_fd, STRLEN * (*i), SEEK_SET);
    int len = STRLEN * occupied_lines;
    while (len != 0 && (ret_read = read(input_fd, buffer, len)) != 0)
    {
        if (ret_read == -1)
        {

            perror("read");
            break;
        }
        len -= ret_read;
        buffer += ret_read;
    }

    for (int j = 0; j < 4096; j++)
    {
        if (buffer[j] == ' ')
        {
            break;
        }
        if (buffer[j] == '\n')
        {
            continue;
        }
        if (buffer[j] == find_str[0])
        {
            int k = 0;
            int p = 0;
            int m = STRLEN;
            for (int l = 1; l < m; l++)
            {
                if (buffer[j + l] == ' ')
                {
                    break;
                }
                if (buffer[j + l] == '\n')
                {
                    m++;
                    p++;
                    continue;
                }
                if (buffer[j + l] != find_str[l - p])
                {
                    k = 1;
                    l = strlen(find_str);
                }
            }
            if (k == 0)
            {
                ret->index[ret->n] == STRLEN *(*i) + j;
                ret->n += 1;
            }
        }
    }
    return ret;
}

int main(int argc, char *argv[])
{
    int lines;
    int status;
    pthread_t thread_id_arr[1024];
    char buffer[6];
    int *arg;
    my_ret *ret;

    find_str = argv[1];
    int n_threads = atoi(argv[2]);
    input_fd = open(argv[3], O_RDONLY);
    int output_fd = open(argv[4], O_CREAT | O_WRONLY | O_TRUNC, 777);
    int _strlen = strlen(find_str);

    read(input_fd, buffer, STRLEN);
    lines = atoi(buffer);
    occupied_lines = (double)lines / n_threads + 0.999;

    for (int i = 0; i < n_threads; i++)
    {
        status = pthread_create(&thread_id_arr[i], NULL, thread_routine, &arg);
        if (status != 0)
        {
            perror("create");
            exit(1);
        }
    }
    char line_change[] = {"\n"};
    for (int i = 0; i < n_threads; i++)
    {
        status = pthread_join(thread_id_arr[i], (void **)&ret);
        for (int j = 0; j < ret->n; j++)
        {
            sprintf(buffer, "%d", ret->index[j]);
            write(output_fd, buffer, strlen(buffer));
            write(output_fd, line_change, 1);
        }
    }
    return 0;
}