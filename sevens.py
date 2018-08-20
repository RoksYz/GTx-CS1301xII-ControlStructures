
def lucky_sevens(a_string):
    sevens = 0
    strings= '7'

    for s in a_string:
        if s ==  strings:   
            sevens+=1

    if sevens == 3:
        return True
    else:
        return False

print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))
