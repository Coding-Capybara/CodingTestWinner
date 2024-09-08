#게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이 구하기
#좌표평면의 경계를 넘는다면 무시

#1. 현재 좌표 저장
#2. U,R,D,L 이 입력될 때 좌표이동
#3. list - 현재 좌표에서 이동할 때 마다, 이동한 좌표를 (,) 형태로 저장. 만약 (-5,-5), (-5,5), (5,5), (5,-5)를 넘어가면 continue
#4. 3번의 list set, 개수 return

#실패, 6~20
#U,R,D,L = (0,1), (1,0), (0,-1), (-1,0)
def solution(dirs):
    nr, nc = 0, 0 #현재 캐릭터 위치
    maps = []
    for i in range(len(dirs)):
        maps.append((nr,nc))
        if dirs[i] == 'L':
            nnr, nnc = nr-1, nc
        if dirs[i] == 'U':
            nnr, nnc = nr, nc+1
        if dirs[i] == 'R':
            nnr, nnc = nr+1, nc
        if dirs[i] == 'D':
            nnr, nnc = nr, nc-1
            
        #한 칸 이동할 때 캐릭터의 위치가 경계를 넘어갔다면 무시
        if nnr < -5 or nnr > 5 or nnc < -5 or nnc > 5: 
            continue
        nr, nc = nnr, nnc
        
    return len(set(maps))

#실패, 8~20
def solution(dirs):
    nr, nc = 0, 0 #현재 캐릭터 위치
    maps = []
    for i in range(len(dirs)):
        if dirs[i] == 'L':
            nnr, nnc = nr-1, nc
        if dirs[i] == 'U':
            nnr, nnc = nr, nc+1
        if dirs[i] == 'R':
            nnr, nnc = nr+1, nc
        if dirs[i] == 'D':
            nnr, nnc = nr, nc-1
            
        #한 칸 이동할 때 캐릭터의 위치가 경계를 넘어갔다면 무시
        if nnr < -5 or nnr > 5 or nnc < -5 or nnc > 5: 
            continue
        maps.append((nr,nc,nnr,nnc))
        nr,nc = nnr, nnc
    return len(set(maps))

#성공
#원인 : 왔던 길을 되돌아 가는 경우(RL)에서 (nr,nc,nnr,nnc) = (nnr,nnc,nr,nc). 둘을 같은 경우로 보고 지워야 함
def solution(dirs):
    nr, nc = 0, 0 #현재 캐릭터 위치
    maps = []
    for i in range(len(dirs)):
        if dirs[i] == 'L':
            nnr, nnc = nr-1, nc
        if dirs[i] == 'U':
            nnr, nnc = nr, nc+1
        if dirs[i] == 'R':
            nnr, nnc = nr+1, nc
        if dirs[i] == 'D':
            nnr, nnc = nr, nc-1
            
        #한 칸 이동할 때 캐릭터의 위치가 경계를 넘어갔다면 무시
        if nnr < -5 or nnr > 5 or nnc < -5 or nnc > 5: 
            continue
        maps.append((nr,nc,nnr,nnc))
        maps.append((nnr,nnc,nr,nc))       
        nr,nc = nnr, nnc
        
    return len(set(maps))/2