# Q1 remove vovals from a word

def vovalRem(word):
    retWord = ""
    for i in word:
        if i not in "aeiou":
            retWord += i
    print()

#Q2 check if a word is a pallindrome

def pallindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    return False

#Q3 Reverse a number

def revNumb(num):
    num = str(num)
    num = num[::-1]
    num = int(num)
    return num

#Q4 Flatten a list

def listFlatter(list):
    retList = []
    for i in list:
        for x in i:
            retList.append(x)

#Q5 Pallindrome of tuple

def tupPallindrome(inTup):
    for i in range(0,int(len(inTup)/2),1):
        if inTup[i] != inTup[(i+1)*(-1)]:
            return False
    return True

print(tupPallindrome((1,1,3,4,4,3,1,1)))
