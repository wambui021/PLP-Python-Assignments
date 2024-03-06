def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    result = calculate_discount(original_price, discount_percent)
    
    print("Final price after applying the discount:", result)

except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")
