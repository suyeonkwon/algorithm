n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = -1000000001
min_result = 1000000001

def solution(num, idx, add, sub, mul, div):
    global min_result, max_result
    if idx == n:
        max_result = max(max_result,num)
        min_result = min(min_result,num)
        return
    if add > 0:
        solution(num + number[idx],idx+1,add-1,sub,mul,div)
    if sub > 0:
        solution(num - number[idx],idx+1,add,sub-1,mul,div)
    if mul > 0:
        solution(num * number[idx],idx+1,add,sub,mul-1,div)
    if div > 0:
        tmp = 0
        if num < 0:
            num = 0 - num
            tmp = num // number[idx]
            tmp = 0 - tmp
        else:
            tmp = num // number[idx]
        solution(tmp,idx+1,add,sub,mul,div-1)

solution(number[0],1,add,sub,mul,div)

print(max_result)
print(min_result)
