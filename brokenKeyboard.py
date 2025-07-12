def findBrokenKeys(str1, str2):
    
    answer = []

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if str1[i] not in answer:
                answer.append(str1[i])

    return answer


print(findBrokenKeys("happy birthday","hawwy birthday"))
print(findBrokenKeys("starry night", "starrq light"))
print(findBrokenKeys("beethoven", "affthoif5"))
print(findBrokenKeys("my name is gonan", "mi nvma es ganon"))
