def solution(record):
    ids = {}
    for r in record:
        log = list(r.split())
        if log[0] == 'Enter' or log[0] == "Change":
            ids[log[1]] = log[2]
    exchange = []
    for r in record:
        log = list(r.split())
        if log[0] == 'Enter':
            exchange.append(f"{ids[log[1]]}님이 들어왔습니다.")
        elif log[0] == "Leave":
            exchange.append(f"{ids[log[1]]}님이 나갔습니다.")

    return exchange