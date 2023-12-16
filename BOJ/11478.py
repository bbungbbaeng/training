str = input()
set = set()

for i in range(len(str)):
  for j in range(i, len(str)):
    set.add(str[i:j+1]) # 슬라이싱으로 가능한 문자열들을 생성, set 집합에 넣어서 중복 제거

print(len(set))
