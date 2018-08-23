
def find_total_exp(points,lucky_egg=False,multiplier=1):

    if lucky_egg:
        points*=2
    else:
        points=points
    hs = points * multiplier
    return int(hs)
    

print(find_total_exp(100))
print(find_total_exp(100, lucky_egg = True))
print(find_total_exp(100, multiplier = 1.5))
print(find_total_exp(100, lucky_egg = True, multiplier = 1.5))