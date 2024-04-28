import math

def solution(a, b, g, s, w, t):
    answer = 0

    left = 1
    # 무게 최대 x 금,은 2 x 거리 최대 x 왕복 2 x 트럭이 가능한 무게 1
    right = (10**9) * 2 * (10**5) * 2 * 1
    
    while left <= right:
        mid = (left + right) // 2
        gold = 0
        silver = 0
        total = 0
        
        for i in range(len(g)):
            # 도시 하나 정보
            total_weight = g[i] + s[i]
            # transport = math.ceil(total_weight / w[i])
            # transport = math.ceil(mid / (t[i] * 2))
            
            transport = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i]:
                transport += 1
                
            possible = transport * w[i]
        
            if g[i] < possible:
                gold += g[i]
            else:
                gold += possible
                
            if s[i] < possible:
                silver += s[i]
            else:
                silver += possible
            
            if total_weight < possible:
                total += total_weight
            else:
                total += possible
        
        if total >= a + b and gold >= a and silver >= b:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer
