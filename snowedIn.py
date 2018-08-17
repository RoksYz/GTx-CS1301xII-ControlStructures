
def  snowed_in(temperature,weather,is_celsius=True):
    if is_celsius == False and temperature < 32:
        return True
    elif is_celsius == True and temperature < 0:
        return True
    elif weather == "snowy":
        return True
    else:
      return False




print(snowed_in(15, "sunny")) #Should print False
print(snowed_in(15, "sunny", is_celsius = False)) #Should print True
print(snowed_in(15, "snowy", is_celsius = True)) #Should print True


