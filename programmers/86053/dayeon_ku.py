def solution(a, b, g, s, w, t):
    answer = 0
    left = 0
    right = (10 ** 9 * 2) * (10 ** 5 * 2)
    
    while left <= right:
        total = 0
        gold = 0
        silver = 0
        mid = (left + right) // 2
        for i in range(len(g)):
            move_count = mid // (t[i] * 2)
            
            if t[i] <= (mid % (t[i] * 2)):
                move_count += 1
                
            gold += w[i] * move_count if w[i] * move_count <= g[i] else g[i]
            silver += w[i] * move_count if w[i] * move_count <= s[i] else s[i]
            total += w[i] * move_count if w[i] * move_count <= g[i] + s[i] else g[i] + s[i]
            
        if gold >= a and silver >= b and total >= a + b:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer