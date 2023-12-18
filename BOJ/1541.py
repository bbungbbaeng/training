exp = input()
array = []
cnt = 0

for i in range(len(exp)):
  if len(exp) == 1:
    array.append(exp[i])
  else:
    if 0 < i < (len(exp) - 1):
      if (exp[i] == '+') or (exp[i] == '-'):
        array.append(exp[i - cnt:i])
        array.append(exp[i])
        cnt = 0
      else:
        cnt += 1
        continue
    elif i == 0:
      cnt += 1
    else:
      array.append(exp[i - cnt:])

flag = False
ans = 0

for i in range(len(array)):
  if (array[i] == '-'):
    flag = True

  if flag:
    if (array[i] == '+') or (array[i] == '-'):
      continue
    else:
      ans -= int(array[i])
  else:
    if (array[i] == '+'):
      continue
    else:
      ans += int(array[i])

print(ans)
