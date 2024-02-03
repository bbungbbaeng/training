n, m = map(int, input().split())
board = list(map(int, input().split()))
sum = board[0]
left, right = 0, 1
cnt = 0

while 1:
    if sum < m:
        if right < n:
            sum += board[right]
            right += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= board[left]
        left += 1
    else:
        sum -= board[left]
        left += 1
print(cnt)
