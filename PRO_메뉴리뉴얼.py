from itertools import combinations

def solution(orders, course):
    answer = []
    alpha = []
    for orde in orders:
        for a in orde:
            if a not in alpha:
                alpha.append(a)

    for num in course:
        comb = list(combinations(alpha, num))
        comb.sort(key=lambda x: (x[0], x[1]))
        cnts = [0] * len(comb)
        for i in range(len(comb)):
            cnt = 0
            for p in orders:
                for c in comb[i]:
                    if c not in p:
                        break
                else:
                    cnt += 1
            cnts[i] = cnt
        max_cnt = max(cnts)
        if max_cnt < 2:
            continue
        for j in range(len(cnts)):
            if cnts[j] == max_cnt:
                # tmp =
                answer.append(''.join(sorted(comb[j])))
    answer.sort()
    return answer


order = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
cour = [2, 3, 4]
print(solution(order, cour))