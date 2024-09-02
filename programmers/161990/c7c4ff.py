def solution(wallpaper):
    
    lux, luy = 51, 51
    rdx, rdy = 0, 0
    
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            lux = min(i, lux)
            luy = min(wallpaper[i].find("#"), luy) # 앞에서부터 찾기
            rdx = max(i+1, rdx)
            rdy = max(wallpaper[i].rfind("#")+1, rdy) # 뒤에서부터 찾기 
            
    return [lux, luy, rdx, rdy]
