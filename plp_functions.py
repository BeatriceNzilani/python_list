def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount= price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price       
    else:
        return price   



price_item = float(input("Enter price of item: "))  
discount_issued = float(input("Enter the discount: "))


final_price= calculate_discount(price_item,discount_issued)
print(final_price)





