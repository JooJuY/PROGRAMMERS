def solution(clothes):
    ans = 1
    dic = {}
    for name, cate in clothes:
        if cate in dic:
            dic[cate].append(name)
        else:
            dic[cate] = [name]
    for d in dic.values():
        ans *= (len(d)+1)
    return ans - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))