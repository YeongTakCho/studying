import os
import os.path
import requests
from bs4 import BeautifulSoup
from settings import path


def makeAcmicpcProblem():

    print('!!! WARNING : IT IS ONLY FOR ACMICPC.NET PROBLEM URL !!!')

    url = input('input url: ')

    if url[:32] != 'https://www.acmicpc.net/problem/':

        print('\n THAT IS WRONG URL, PLEASE CHECK YOUR URL\n')
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    title = str(soup.select('title'))
    print(title)
    problem_num = url[32:]
    problem_name = title[len(problem_num)+11:-9]

    file_name = path + problem_num + '- ' + problem_name + '.py'
    try:
        f = open(file_name, 'w', encoding="UTF-8")
    except:
        print('file name error. enter new problem name: ', end='')
        problem_name = input()
        file_name = path + problem_num + '- ' + problem_name + '.py'
        f = open(file_name, 'w', encoding="UTF-8")

    txt = '# SOLVING code for "BOJ {0}. {1}"\n#- Problem link: {2}\n#- MY link:\n#- Used algorithm:'.format(
        problem_num, problem_name, url)
    f.write(txt)
    f.close


makeAcmicpcProblem()
