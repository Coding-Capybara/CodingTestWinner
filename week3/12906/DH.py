def solution(arr):
    answer = [arr[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr:
        if answer[-1] == i:
            continue
        else:
            answer.append(i)
    return answer