participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
  #index끼리 비교하기 위해 먼저 정렬
    participant.sort()
    completion.sort()

  #해당 인덱스 값을 서로 비교하여 다르면 return
    for i in range(len(participant)):
        val = participant[i]
        val2 = completion[i] if i < len(completion) else ""
        if(val != val2):
            return val

print(solution(participant,completion))
