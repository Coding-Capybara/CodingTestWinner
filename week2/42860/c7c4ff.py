def alter_ord(alphabet):
  # 조이스틱 위아래 조작
  # 앞에서부터 세는 경우, 뒤에서부터 세는 경우 중 작은 쪽으로
    return min(ord(alphabet) - ord("A"), ord("Z") - ord(alphabet) + 1)
    
def solution(name):
    move = len(name) - 1 # 오른쪽으로만 진행했을 경우를 상정
    answer = 0

    for idx in range(len(name)):
        answer += alter_ord(name[idx]) 
        next_idx = idx + 1
        
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
            
        print(idx, len(name) - next_idx)

        # 현재까지 움직인 거리 (오른쪽으로만), 왼쪽으로 옮겨 다녀오는 거리 중 짧은 거리 선택
        distance = min(idx, len(name) - next_idx)
        # idx: 오른쪽으로 진행한 거리
        # len(name) - next_idx: 왼쪽으로 다녀온 적이 있으면 그만큼의 거리가 됨. 오른쪽으로 전부 이동해보며 뒤에 A가 연속해 있다면 자연스레 줄어듦
        # distance: (필요하다면) 왼쪽으로 다녀온 거리
        move = min(move, idx + len(name) - next_idx + distance)

    return answer + move
