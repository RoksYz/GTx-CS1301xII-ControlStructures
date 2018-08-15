egg = True
milk = True
butter = True
flour = True
#
# 1. pancakes: egg, milk, butter, flour
# 2. omelette: egg, milk, butter
# 3. custard: egg, milk
# 4. poached eggs: egg
#
#The list above is also a priority list. If you have the
#ingredients for pancakes, you'll make pancakes instead of
#any of the other dishes. If you're missing flour but have
#the other ingredients, you'll make an omlette. You'll only
#make poached eggs if the only ingredient you have is eggs.
#
#Complete the program below such that it prints which dish
#you'll make based on the ingredients you have handy. All
#the dishes should appear exactly as shown above: all lower
#case, spelled the same way. If you do not have the
#ingredients to make any of these dishes, then print the
#text "Go to the store!"

if egg, milk, butter, flour:
    print("pancakes")
elif egg,milk,butter:
    print("omelette")
elif egg,milk:
    print("custard")
elif egg:
    print("eggs")
else:
    print("Go to the store!")