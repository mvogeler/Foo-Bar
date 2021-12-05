def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_list(list):
    length = len(list)
    out = 0
    for i in range(0, length):
        out = gcd(out, list[i])
    return out


def fuse(v1, i1, v2, i2):
    length_v = len(v1)
    indices = (set(range(length_v)) - {i1, i2})
    sum2 = sum(v2)
    out = [0 for _ in v1]
    for i in indices:
        out[i] = sum2 * v1[i] + v1[i2] * v2[i]
    gcd_val = gcd_list(out)
    return [int(i / gcd_val) for i in out]


def solution(m):
    height = len(m)
    mat = list(m)
    for i, element in enumerate(mat):
        element[i] = 0
    sums = [sum(i) for i in mat]
    terms = [i for i, item in enumerate(sums) if item == 0]
    not_terms = list((set(range(height)) - set(terms)))

    length = len(not_terms)

    for i in range(0, length - 1):
        index_b = not_terms[length - i - 1]
        for j in range(0, length - 1):
            index_a = not_terms[j]
            mat[index_a] = fuse(mat[index_a], index_a, mat[index_b], index_b)
    output = []
    for i in terms:
        output.append(mat[0][i])
    tot = sum(output)
    output.append(tot)
    if tot == 0:
        output = [1 for _ in terms]
        output.append(len(terms))
    return output
