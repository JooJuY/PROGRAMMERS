def solution(s):
    answer = ''
    nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    i = 0
    num = ''
    while i < len(s):
        if '0' <= s[i] <= '9':
            answer += s[i]
        else:
            num += s[i]
            if num in nums:
                answer += nums[num]
                num = ''
        i += 1
    return int(answer)


s1 = "one4seveneight"
s2 = "23four5six7"
s3 = "2three45sixseven"
s4 = "123"

print(solution(s4))