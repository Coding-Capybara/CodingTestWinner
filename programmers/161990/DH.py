def solution(wallpaper):
    answer = []
    garos=[]
    seros=[]
    for sero in range(len(wallpaper)):
        for garo in range(len(wallpaper[sero])):
            if wallpaper[sero][garo] == "#":
                seros.append(sero)
                garos.append(garo)
            else:
                pass
    lux = min(seros)
    luy = min(garos)
    rdx = max(seros)+1
    rdy = max(garos)+1
    answer = [lux, luy, rdx, rdy]
    return answer