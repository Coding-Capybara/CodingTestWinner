def solution(wallpaper):
    first_row, first_col, last_row, last_col = 51, 51, 51, -1
    
    # y 찾기
    for row in range(len(wallpaper)):
        # 업데이트되면 바로 loop 나가기
        if first_row != 51 and last_row != 51:
            break
        
        if first_row == 51 and "#" in wallpaper[row]:
            first_row = row
        
        if last_row == 51 and "#" in wallpaper[-(row+1)]:
            last_row = len(wallpaper) - row
            
    # x 찾기
    for row in wallpaper:
        for col in range(len(row)):
            if col < first_col and row[col] == "#":
                first_col = col
                
            if len(row) - col > last_col and row[-(col+1)] == "#":
                last_col = len(row) - col
                
    return [first_row, first_col, last_row, last_col]

    