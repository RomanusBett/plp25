def calculate_discount(price, discount_percent):
    if int(discount_percent) >= 20:
        return round(((100-int(discount_percent))/100)*int(price))
    else:
        return int(price)
    
item_price = input('Enter the price of the item')
discount_percentage = input('Enter the discount')

print(calculate_discount(item_price, discount_percentage))