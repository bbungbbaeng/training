# 피타고라스 정리를 이용한 수학 문제
# d^2 = ((h * r)^2 + (w * r)^2) ** 0. 5
# d = r(h^2 + w^2) ** 0.5
# r = d / (h^2 + w^2) ** 0.5
# r을 h, w에 곱해주면 원래의 길이를 알 수 있음

d, h, w = map(int, input().split())

r = d / (h ** 2 + w ** 2) ** 0.5

print(int(h * r), int(w * r))
