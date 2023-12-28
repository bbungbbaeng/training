while 1:
    try:
        text = input()
        ans = [0 for i in range(4)]
        for i in text:
            if i.islower():
                ans[0] += 1
            elif i.isupper():
                ans[1] += 1
            elif i.isdigit():
                ans[2] += 1
            elif i == ' ':
                ans[3] += 1
        print(ans[0], ans[1], ans[2], ans[3])
    except:
        break

# try - except 구문
# 에러가 발생하는 상황에서 예외를 처리할 수 있는 구문
# 해당 문제는 문자열이 N번 입력된다고 했는데, N을 입력으로 받지 않음
# 그러므로, while 반복문을 실행시킨 후 입력이 지속되지 않을 경우 예외 처리에 의해 반복문이 종료됨
