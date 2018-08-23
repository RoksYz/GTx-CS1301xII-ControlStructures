days_since_release = 700
original_price = 60
greatest_hits = True



#
#Assume that a new release loses $2 off its price for every
#full week since it was released. So, two full weeks (14 days)
#after a $60 game is released, it will cost $56.
#
#However, if the release is considered a "greatest hit", it
#loses value half as fast: after two weeks, it will be $58
#instead of $56.
#
#No release will ever fall to below $20, however, no matter
#how fast it loses value or whether it's a greatest hit.
#
#Add some code below to print the current price of the release.
#For example, with the values above, it would pring $58.
week = 7
now = days_since_release // week
prices = 2

if greatest_hits:
    prices -= 1

maxs = 20
final = original_price - (now * prices)

if final < 20:
    final = maxs
else:
    final = final
   
print("${}".format(final))