genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    dic_genres = {}
    dic_plays = {}
    
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g not in dic_genres :
            dic_genres[g] = p
        else :
            dic_genres[g] += p
        
        if g not in dic_plays:
            dic_plays[g] = [(i,p)]
        else:
            dic_plays[g].append((i,p))
    
    for (g,p) in sorted(dic_genres.items(), key = lambda x : x[1], reverse = True):
        for (i,k) in sorted(dic_plays[g], key = lambda x : x[1], reverse = True)[:2]:
            answer.append(i)
            
    return answer

print(solution(genres, plays))
