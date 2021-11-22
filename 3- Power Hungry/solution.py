def solution(xs):
    prod = 1

    if all(e == 0 for e in xs):
        return "0"

    if len(xs) == 1 and xs[0] < 0:
        return str(xs[0])

    if len([e for e in xs if e != 0]) == 1 and min(xs) < 0:
        return "0"

    for e in xs:
        if e != 0 and e <= 1000:
            prod *= e
    return str(prod) if prod >= 0 else str(prod/max([n for n in xs if n < 0]))

