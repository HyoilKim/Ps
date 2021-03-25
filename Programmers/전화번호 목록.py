def solution(phone_book):
    phone_book.sort()
    dic = {}
    for phone_number in phone_book:
        dic[phone_number] = True
    for phone_number in phone_book:
        prefix = ""
        for i in phone_number:
            prefix += i
            if dic.get(prefix, False) and prefix != phone_number:
                print(prefix)
                return False
    return True