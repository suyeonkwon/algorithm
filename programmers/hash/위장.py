from collections import Counter

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    kind = []
    result = 1

    #Counter 사용하기 위해 옷 종류만 다시 list로 생성
    for i in clothes:
        kind.append(i[1])
    
    #Counter사용하여 종류별 갯수를 count하여 딕셔너리로 변환
    dic = dict(Counter(kind))
    
    #옷 개수 + 1 (옷을 입지 않는 경우도 고려)
    for i in dic.keys():
        result *= (dic.get(i)+1)
    
    #아무것도 입지 않는 경우는 없으므로 -1
    return result-1

print(solution(clothes))
