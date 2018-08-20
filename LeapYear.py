
def is_leap_year(year):
    if year % 4==0 and not year % 100==0 :
        return True
    
    elif year%400==0:
        return True
    elif year %100==0:
        return False
    else:
        return False

print("1993 is a leap year:", is_leap_year(1993))
print("1996 is a leap year:", is_leap_year(1996))
print("1900 is a leap year:", is_leap_year(1900))
print("2000 is a leap year:", is_leap_year(2000))