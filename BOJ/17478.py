def rcs1(n):
    for i in range(n + 1):
        if i == 0:
            print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
            print('"재귀함수가 뭔가요?"')
            print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
            print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
            print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        elif i == n:
            print('____' * i, end = '')
            print('"재귀함수가 뭔가요?"')
            print('____' * i, end = '')
            print('"재귀함수는 자기 자신을 호출하는 함수라네"')
            print('____' * i, end = '')
            print('라고 답변하였지.')
        elif 0 < i < n:
            print('____' * i, end = '')
            print('"재귀함수가 뭔가요?"')
            print('____' * i, end = '')
            print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
            print('____' * i, end = '')
            print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
            print('____' * i, end = '')
            print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

def rcs2(n):
    for i in range(n):
        print('____' * (n - i - 1), end = '')
        print('라고 답변하였지.')

n = int(input())
rcs1(n), rcs2(n)