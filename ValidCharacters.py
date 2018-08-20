
def is_valid(valid_string,valid_characters):

    testcheck = valid_string
    valid = set(valid_characters)

    if set(valid).issubset(testcheck):
        return True
    else:
        return False
    
sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))