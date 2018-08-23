def num_factors(count):
    total = 0
    for x in range(2,count):
        if count % x == 0:
            total +=1
    return total


print(num_factors(5))
print(num_factors(6))
print(num_factors(97))
print(num_factors(105))
print(num_factors(999))