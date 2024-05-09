def solution(N, number):
    # target과 N이 동일한 경우
    if N == number:
        return 1
    # 중복 제거를 위해 set()
    dp = [set() for _ in range(9)]
    # N을 연결한 숫자 추가
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
    # dp[2]부터 시작
    for i in range(2,9):
        # i를 만들 수 있는 경우의 수
        # j가 i-j보다 큰 경우만을 가정
        # 반대의 경우는 -와 //만 순서를 바꿔주면 가능 
        for j in range(1, i//2+ 1):
            print(j, i-j, i)
            for n1 in dp[j]:
                for n2 in dp[i-j]:  
                    dp[i].add(n1+n2)
                    dp[i].add(n1-n2)
                    dp[i].add(-n1+n2)
                    dp[i].add(n1*n2)
                    if n2 != 0:
                        dp[i].add(n1//n2)
                    if n1 != 0:
                        dp[i].add(n2//n1)
        if number in dp[i]:
            return i
    return -1