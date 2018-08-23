def remove_capitals(ss):

    hc =  (word for pair in ss for word in pair if not word.isupper())

    ss = ''.join(hc)
    
    return ss

print(remove_capitals("A1B2C3D"))
print(remove_capitals("Georgia Institute of Technology"))
