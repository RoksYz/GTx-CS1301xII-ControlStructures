story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
total = 0
if story =="A":
    total+=6
elif story=="B":
    total+=5
elif story=="C":
    total+=4
elif story=="D":
    total+=2
else:
    total=total

if text =="A":
    total+=5
elif text=="B":
    total+=4
elif text=="C":
    total+=3
elif text=="D":
    total+=1

if role =="A":
    total+=4
elif role=="B":
    total+=3
elif role=="C":
    total+=2
elif role=="D":
    total+=director
else:
    total=total

if director =="A":
    total+=3
elif director=="B":
    total+=2
elif director=="C":
    total+=1
else:
    total=total

if cast =="A":
    total+=2
elif cast=="B":
    total+=1

else:
    total=total

print(total)

if total >= 20:
    print("Perfect score")
elif total >=17:
    print("Must do")
elif total >=14:
    print("Seriously consider")
elif total >=12:
    print("On the bubble")
else:
    print("Pass")



