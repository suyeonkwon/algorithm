def solution(citations):
    citations.sort()
    length = len(citations)
    for h in range(length):
        if(citations[h] >= length-h):
            return length-h
    return 0
