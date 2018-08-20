
def find_pressure(moles,temperature,volume,r=0.082057):
    s = moles*r*temperature
    p = s / volume
    
    return p 

test_n = 10
test_T = 298
test_V = 5
test_R = 62.364

print("Result:", find_pressure(test_n, test_T, test_V,r=test_R))