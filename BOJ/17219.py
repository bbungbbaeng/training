n, m = map(int, input().split())
link = dict()
idk = list()

def find_pwd(): # 비밀번호를 찾고 싶은 사이트 조회 함수
  yourpwd = list()
  for i in idk: # idk의 사이트를 link의 key로 하여 value를 찾는다
    yourpwd.append(link[i])
  return '\n'.join(yourpwd) # join으로 리스트를 줄바꿈이 된 문자열로 변환

for i in range(n + m):
  if i <= n - 1:
    a = input().split()
    link[a[0]] = a[1]
  else:
    idk.append(input())

print(find_pwd())
