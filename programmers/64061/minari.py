#moves 위치의 가장 윗칸 인형을 뽑아 basket에 더하기
#만약 뽑은 인형이 basket의 가장 윗칸 인형과 같다면, basket.pop, answer += 2
#moves가 끝날때까지 반복진행
#1. moves 갯수만큼 for문 돌기
#2. 만약 moves위치에 아무 인형도 없으면 실행x
#3. 만약 basket이 차있고, basket의 가장 윗 위치 인형이 moves위치의 가장 윗 인형과 같다면 moves위치 가장 윗 인형자리 = 0, basket.pop, answer += 2
#4. else: moves위치의 가장 윗 인형 뽑아서 board에 저장, moves위치의 가장 윗 인형 자리 = 0 
def solution(board, moves):
    answer = 0
    basket = []
    #1.
    for i in moves:
        for j in range(len(board)): #len(board) : column갯수. 차있는 인형의 위치를 모르기 때문에..
            if board[j][i-1] > 0:
                #3.
                if basket and board[j][i-1] == basket[-1]:
                    board[j][i-1] = 0
                    basket.pop()
                    answer += 2
                #4.
                else:    
                    basket.append(board[j][i-1])
                    board[j][i-1] = 0
                break
            #2.
            else:
                pass
            
    return answer