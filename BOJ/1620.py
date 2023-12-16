n, m = map(int, input().split())
pokemon = dict()
quiz = list()

for i in range(n + m):
  if i <= n - 1:
    pokemon[input()] = i + 1
  else:
    quiz.append(input())

r_pokemon = {str(v): k for k, v in pokemon.items()} # pokemon 딕셔너리의 키와 밸류 값의 위치를 전환한 딕셔너리 생성

for i in quiz:
  if i in pokemon.keys():
    print(pokemon[i])
  elif i in r_pokemon.keys():
    print(r_pokemon[i])
