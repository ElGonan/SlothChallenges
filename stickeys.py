def isLongPressed(original, typed):
    # My starting pointers
    originalval = 0
    typedval = 0

    # The usually largest input
    while typedval < len(typed):
        # if both characters are the same, step
        if originalval < len(original) and original[originalval] == typed[typedval]:
            originalval += 1
            typedval += 1
        # if the character is the same as the one I had earlier, step.
        elif typedval > 0 and typed[typedval] == typed[typedval - 1]:
            typedval += 1
        else:
            # break and return.
            print("false")
            return

    # If i went through all the array, succeed.
    if originalval == len(original):
        print("true")
    else:
        print("false")

isLongPressed("alex","aaaaaleex")
isLongPressed("saeed","ssaaedd")
isLongPressed("leelee","lleeelee")
isLongPressed("Tokyo","TTokkyoh")
isLongPressed("laiden","laiden")



