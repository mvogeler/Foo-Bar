def solution(l, t):
    for i in range(len(l) + 1):
        for j in range(i):
            total = sum(l[j: i])
            if total == t:
                return [j, i - 1]
            elif total > t:
                continue
    return [-1, -1]
