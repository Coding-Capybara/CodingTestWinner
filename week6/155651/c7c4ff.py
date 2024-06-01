from heapq import heappop, heappush

def solution(book_time):
    rooms = []
    book_time.sort(key = lambda _:_[0])
    print(book_time)
    
    for res in book_time :
        check_in = calculate_time(res[0])
        check_out = calculate_time(res[1]) + 10
        if len(rooms) != 0 and rooms[0] <= check_in :
            heappop(rooms)
        heappush(rooms, check_out)
    return len(rooms)

def calculate_time(time) :
    return int(time[:2])*60 + int(time[3:])
