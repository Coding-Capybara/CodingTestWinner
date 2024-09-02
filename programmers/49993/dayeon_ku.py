def solution(skill, skill_trees):
    answer = 0
    # 알파벳 분리해주기
    skill_list = [*skill]
    index_list = []
    
    # 유저가 만든 skill tree 하나씩 돌기
    for st in skill_trees:
        # temp에 지정한 skill 순서대로(인덱스 1씩 증가) 들어가는지 확인할 b
        b = True
        temp = []
        for char in st:
            # try로 skill에 있는 알파벳만 취급                
            try:
                flag = skill_list.index(char)
                # temp에 아무것도 없으면 추가
                if not temp:
                    temp.append(flag)
                else:
                    # temp에 들어가는 인덱스가 1씩 증가하면 추가
                    if temp[-1] + 1 == flag:
                        temp.append(flag)
                    # 아니라면 b = False로 놓고 break
                    else:
                        b = False
                        break
            except:
                pass
        # b가 True인 경우에만 index_list에 추가
        if b:
            index_list.append(temp)
        
    for l in index_list:
        # skill에 없는 스킬만 있는 스킬 트리였다면
        if not l:
            answer += 1
        # 인덱스가 0으로 시작하면
        elif l[0] == 0:
            answer += 1
    
    return answer