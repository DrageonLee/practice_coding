'''후위 표기식
중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있 으면 중위표기식입니다.
후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
(3+5)*2 이면 35+2* 로 바꾸어야 합니다.
※후위 표기식이 이해가 안되면 구글링으로 공부해보는 것도 좋습니다.

- 입력 설명
첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다. 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.

- 출력 설명
후위표기식을 출력한다.

'''
#내가 푼 것(오답 - 두 번째 예제에서 오답)
from curses.ascii import isdigit
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
equation = input()

stack = []
post_equation = ''
for i in range(len(equation)) :
    if isdigit(equation[i]) :
        post_equation += equation[i]
        if equation[i-1] == '*' or equation =='/':
            post_equation += stack.pop()
    elif equation[i] == ')':
        for i in range(len(stack)):
            if stack[-1] != '(' :
                post_equation += stack.pop()
            else :
                stack.pop()
                break
    else :
        stack.append(equation[i])
if stack :
    for i in range(len(stack)):
        post_equation += stack.pop()        

print(post_equation)



#다른 문제 풀이(정답)
from curses.ascii import isdigit
import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
equation = input()
stack = []
res = ''

for i in equation:
    if i.isdecimal() :
        res += i
    else :
        if i == '(':
            stack.append(i)
        elif i == '*' or i =='/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.append(i)
        elif i ==')':
            while stack and stack[-1] != '(' :
                res+= stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)