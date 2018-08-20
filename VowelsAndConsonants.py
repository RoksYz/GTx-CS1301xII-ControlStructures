
def count_letters(a_string,find_consonants):

    a_string = a_string.lower()
    vowels = 'aeiou'
    consonants = "bcdfghjklmnpqrstvwxzy"

    numsV = 0
    numsC = 0

    if find_consonants == True:
        for s in a_string:
            if s in consonants:
                print(s)
                numsV+=1
        return numsV
    elif find_consonants == False:
        for s in a_string:
            if s in vowels:
                numsC+=1
        return numsC

a_string = "sunlight estimable wetland ecstasy"

print(count_letters(a_string, True))
print(count_letters(a_string, False))