phase = "Full"
distance = 228000
date = 31
eclipse = True

if phase == "Full":
    moonresult = " "
    if distance < 230000:
        moonresult+= " Super"

    if date >=29:
        moonresult+= " Blue"

    if eclipse == True:
        moonresult+= " Blood"
    if moonresult ==" " :
        print("Full Moon")
    
    else:
        print("{} Moon".format(moonresult))
    
else:
    print('Moon')
