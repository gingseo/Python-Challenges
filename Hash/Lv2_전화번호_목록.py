def solution1(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i + 1].startswith(phone_book[i]):
                return False
    return True

def solution2(phone_book):
    phone_hash = dict()

    for i in phone_book:
        phone_hash[i] = i # phone_hash[hash(i)] 로 하면 해시 값이 항상 달라짐

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num
            if arr in phone_hash and arr != nums:
                return False
            
    return True
        

test = ["119", "5521194421"]
print(solution2(test))

def my_fault_solution(phone_book):
    # 이러면 접두사가 긴 전화보다 뒤에 있으면 해시ㅔ접두사] = 접두사 로 업데이트된다.
    phone_dict = dict()

    for num in phone_book:
        for other_num in phone_book: 
            if other_num.startswith(num):  # 접두사인지 확인
                phone_dict[num] = other_num
    
    for key, value in phone_dict.items():
        if key != value:
            return False
    return True