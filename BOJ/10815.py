n = int(input())
card = set(map(int, input().split()))

m = int(input())
idkcard = list(map(int, input().split()))

for i in idkcard:
  if i in card:
    print(1, end=" ")
  else:
    print(0, end=" ")
