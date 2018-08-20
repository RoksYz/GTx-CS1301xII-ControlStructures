
def word_count(a_string):
    asd = a_string.split()
    nums=0
    for s in asd:
        nums +=1
    return nums
    
def letter_count(a_string):
    numsl=0
    for s in a_string:
        if s != " ":
            numsl+=1

    return numsl

def average_word_length(a_string):
    s =  letter_count(a_string) / word_count(a_string) 

    return s

a_string = "Up with the white and gold"

print(average_word_length(a_string))


