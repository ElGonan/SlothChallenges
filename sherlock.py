# ElGonan
# july 15, 2025


def isValid(input):
    dic = {}

    for i in input:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1

    
    if max(dic.values()) - min(dic.values()) > 0:
            maximum = max(dic, key=dic.get)
            dic[maximum] -= 1

    if max(dic.values()) - min(dic.values()) > 0:
        return "NO"

    return "YES"


print(isValid("abc"))
print(isValid("abcc"))
print(isValid("abccc"))
print(isValid("aabbcd"))
print(isValid("aabbccddeefghi"))
print(isValid("abcdefghhgfedecba"))
