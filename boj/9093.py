t = int(input())

for i in range(t):
    sentence = input()
    result = ''
    tmp = []
    for s in sentence:
        if s == ' ':
            for t in tmp[::-1]:
                result += t
            result += s
            tmp = []
        else:
            tmp.append(s)

    for t in tmp[::-1]:
        result += t
    print(result)
