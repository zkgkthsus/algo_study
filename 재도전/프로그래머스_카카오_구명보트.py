def solution(people, limit):
    # 정렬이 필수
    people.sort()
    s = 0
    idx = len(people) - 1
    answer = 0

    while s <= idx:
        # 반복할 때 마다 횟수는 증가하고
        answer += 1
        # 맨 뒤와 무게를 합했을 때 제한무게를 넘어서면 시작점을 당겨주고
        if people[s] + people[idx] <= limit:
            s += 1
        # 아니면 뒷 좌표만 계속해서 줄여준다
        idx -= 1
    print(s, idx)
    return answer