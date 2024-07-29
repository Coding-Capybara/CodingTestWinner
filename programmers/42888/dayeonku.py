def solution(record):
    _record = list(map(lambda x: [a for a in x.split(" ")], record))
        
    db = {log[1]:log[2] for log in _record if log[0] == "Enter" or log[0] == "Change"}
    result = []
    
    for log in _record:
        el, uid = log[0], log[1]
        if el == "Enter":
            message = f"{db[uid]}님이 들어왔습니다."
        elif el == "Leave":
            message = f"{db[uid]}님이 나갔습니다."
        else:
            continue
            
        result.append(message)
    
    return result