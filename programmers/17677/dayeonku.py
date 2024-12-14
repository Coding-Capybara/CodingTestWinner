# Lv.2 뉴스 클러스터링
import re
from collections import Counter


def create_subword(word):
    pattern = r"[a-z]+"
    result = []
    for i in range(len(word)-1):
        window = word[i:i+2]

        if re.fullmatch(pattern, window):
            result.append(window)
        else:
            continue
                
    return result


def solution(str1, str2):
    # Jacaard = intersection / union
    # A, B 둘 다 empty set일 경우  J(A, B) = 1
    # 다중 집합이면 intersection은 min freq, union은 max freq으로 카운트
    # 특수문자 붙은 문자 제거
    answer = 0
    
    a = create_subword(str1.lower())
    b = create_subword(str2.lower())
    
    if not a and not b:
        return 65536
    else:
        intersection = []
        union = []
        count_a, count_b = Counter(a), Counter(b)
        
        for sub_a, c_a in count_a.items():
            if sub_a in count_b:
                min_freq = min(c_a, count_b[sub_a])
                max_freq = max(c_a, count_b[sub_a])
                intersection.extend([sub_a] * min_freq)
                union.extend([sub_a] * max_freq)
                
                del count_b[sub_a]
            else:
                union.extend([sub_a] * c_a)
        
        if count_b:
            for k, v in count_b.items():
                union.extend([k] * v)
        
        answer = len(intersection) / len(union)

        return int(answer * 65536)