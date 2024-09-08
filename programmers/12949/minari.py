#1. 행렬의 곱셈 결괏값 : (r1,c2), c1=r2일때만 가능
#2. 한 자리에서 곱셈이 더해지는 횟수 : c1=r2
def solution(arr1, arr2):
    r1,c1 = len(arr1), len(arr1[0])
    r2,c2 = len(arr2), len(arr2[0])
    answer = [[0 for _ in range(c2)]for _ in range(r1)]  #(r1, c2), (c1=r2)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer