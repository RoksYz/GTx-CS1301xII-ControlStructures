
def valid_product_code(ss):
    lss = len(ss)
    if lss % 4 == 0:
        if ss.isupper():
            if "A1" in ss:
                return True
            else:
                return False
        else:
            return False
    else: 
        return   False

print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))