'''회문 문자열 검사
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

- 입력설명
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.

- 출력설명
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.
'''

#내 문제 풀이
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
for n in range(N):
    word = input()
    word = word.upper()
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            print(f'#{n+1} No')
            break
    else :
        print(f'#{n+1} Yes')

#다른 문제 풀이(간단하게 python 스럽게)
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
N = int(input())
for n in range(N):
    word = input()
    word = word.upper()
    if word == word[::-1]:
        print(f'#{n+1} Yes')
    else :
        print(f'#{n+1} No')