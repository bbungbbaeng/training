nums = [0, 1, 1]
def seq(n):
    if N == 0:
        return nums[0]
    
    nums[-1] = nums[0] + nums[1] # [0, 1, 1+1]
    nums[0] = nums[1] # [1, 1, 2]
    nums[1] = nums[-1] # [1, 2, 2]

    if n < N - 2: # n이 아직 (N - 2)보다 작다면 (피보나치 수열은 2번째 부터 진행되므로 입력받은 N 값에서 2를 빼줌)
        seq(n + 1) # 재귀
    return nums[-1] # 수열의 합인 nums 리스트의 맨 마지막 값을 반환

N = int(input())
print(seq(0))
