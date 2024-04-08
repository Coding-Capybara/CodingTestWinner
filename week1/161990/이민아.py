def solution(wallpaper):
    ans = []
    x_lst = list()
    y_lst = list()
    #1.
    for i in range(len(wallpaper)): #y의 길이
        for j in range(len(wallpaper[0])): #x의 길이
            if wallpaper[i][j] == '#':
                x_lst.append(i)
                y_lst.append(j)
    #2.
    ans.append(min(x_lst))
    ans.append(min(y_lst))
    ans.append(max(x_lst)+1)
    ans.append(max(y_lst)+1)

    return ans