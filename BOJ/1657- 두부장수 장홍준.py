# SOLVING code for "BOJ 1657. 두부장수 장홍준"
# - Problem link: https://www.acmicpc.net/problem/1657
# - MY link:
# - Used algorithm:
import sys
read = sys.stdin.readline

grade_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
grade_matrix = [[10, 8, 7, 5, 1],
                [8, 6, 5, 3, 1],
                [7, 5, 3, 2, 1],
                [5, 3, 2, 2, 1],
                [1, 1, 1, 1, 0]]


def get_val(first_grade, second_grade):
    return grade_matrix[grade_to_int[first_grade]][grade_to_int[second_grade]]


def sol():
    N, M = map(int, read().split())

    matrix = [list(read().rstrip()) for _ in range(N)]


if __name__ == "__main__":
    print(sol())
