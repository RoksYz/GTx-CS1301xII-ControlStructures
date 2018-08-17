start_character = "A"
end_character = "Z"

s = ord(start_character)

while s != ord(end_character):
    print(chr(s))
    s+=1

print(end_character)