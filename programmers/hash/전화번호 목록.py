phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    #길이가 짧은 번호가 앞으로 오게 정렬
    phone_book.sort()
    
    for z1, z2 in zip(phone_book,phone_book[1:]):
        if(z2.find(z1) == 0):
            return False
          
    return True

print(solution(phone_book))
