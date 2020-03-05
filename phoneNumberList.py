source = ["119", "97674223", "1195524421"]
# source = ["12","123","1235","567","88"]
# source = ["0","789","12", "131"]

def solution(phone_book):
    # token = {}
    def tokenDicEachPhoneNum (prefix, phone_book):
      for phoneNum in phone_book:
        if phoneNum != prefix:
          prefixLen = len(prefix)
          for i in range(len(phoneNum) - (prefixLen - 1)):
            _token = phoneNum[i:i+prefixLen]
            if prefix == _token:
              return False

    answer = True
    # make token dic
    for phone_num in phone_book:
      if False == tokenDicEachPhoneNum(phone_num, phone_book):
        answer = False
        return answer
    
    return answer

result = solution(source)
print('result', result)