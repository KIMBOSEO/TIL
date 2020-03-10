#1 강사님 버전 palindrome!
'''
def palindrome(word):
    list_word = list(word)
    # 0부터 문자열의 길이의 절반만큼 반복
    for i in range(len(list_word) // 2):
        # 왼쪽 문자와 오른쪽 문자를 비교
        if list_word[i] != list_word[-i-1]:
            return False # 회문이 아님
    return True

    print(list_word)

print(palindrome('poolloop'))
print(palindrome('dkdhoaov'))
'''

'''
# 2번째 버전

word = 'eye'
new_word = reversed(word)
print(new_word)
print(''.join(new_word))

def palindrome(word):
    return word == ''.join(reversed(word))   # join 함수의 결과값이 bool이라서 if로 따로 안 나눔
'''


'''
#3 쉬운거

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
'''