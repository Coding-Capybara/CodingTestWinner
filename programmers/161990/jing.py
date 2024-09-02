def solution(wallpaper):
    # "#"가 있는 위치의 x, y 좌표를 각각 저장
    x = []
    y = []
    
    # wallpaper를 돌면서 "#"의 위치와 좌표 확인
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                x.append(i)
                y.append(j)
    
    # 존재하는 "#"를 모두 드래그할 수 있도록 좌표를 출력
    return [min(x), min(y), max(x)+1, max(y)+1]