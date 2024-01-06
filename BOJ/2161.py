from collections import deque

n = int(input())
card = deque([i for i in range(1, n + 1)])

for i in range(n):
    if 0 <= i < n - 1:
        print(card.popleft())
        a = card[0]
        del card[0]
        card.append(a)
    if i == n - 1:
        print(card.pop())
