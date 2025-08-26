def is_valid_hex_code(input):
    valid = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']


    if len(input) != 7:
        return False
    if input[0] != '#':
        return False
    
    for i in range(1, len(input)):
        if input[i].capitalize() not in valid:
            return False
    return True




#test1 = is_valid_hex_code("#CD5C5C")
#print("test1:", test1, "expected: True")

#test2 = is_valid_hex_code("#EAECEE")
#print("test2:", test2, "expected: True")

#test3 = is_valid_hex_code("#eaecee")
#print("test3:", test3, "expected: True")

#test4 = is_valid_hex_code("#CD5C58C")
#print("test4:", test4, "expected: False")
# Length exceeds 6

#test5 = is_valid_hex_code("#CD5C5Z")
#print("test5:", test5, "expected: False")
# Not all alphabetic characters in A-F

#test6 = is_valid_hex_code("#CD5C&C")
#print("test6:", test6, "expected: False")
# Contains unacceptable character

#test7 = is_valid_hex_code("CD5C5C")
#print("test7:", test7, "expected: False")
# Missing #
