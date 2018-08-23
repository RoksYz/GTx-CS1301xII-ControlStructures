
def average_word_length(my_string):

    numsl = 0
    listc = ".",",","!","?"
    try:
        for s in my_string:
            if s != " ":
                if s not in listc:
                    numsl+=1
        if numsl == 0:
            return "no words"
    except:
        return "Not a string" 
    
    result = 0
    try:
        my_string = my_string.split()
        for item in my_string:
            result+=1
    except:
        return "No words"
    final = numsl / result
    return final
#output:
#2.0
#3.0
#4.0
#Not a string
#No words

print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))
