def solution(t:[int]) -> int:
    length = len(t)
    count = 0
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if t[i] + t[j] > t[k] and t[i] + t[k] > t[j] and t[j] + t[k] > t[i]:
                    count += 1
    return count    
    
print(solution([1, 2, 3, 4])) # 4
print(solution([1, 1, 1, 1])) # 0
print(solution([2,2,3,4])) # 4