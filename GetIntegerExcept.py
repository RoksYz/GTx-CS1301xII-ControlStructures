def get_integer(my_var):

    try:
        my_var = int(my_var)
        return my_var

    except Exception as error:
        return (error)

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1)).    
#




