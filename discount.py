def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to apply.

  Returns:
    The final price after applying the discount, or the original price if the discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get user input
original_price = float(input("Enter the original price: "))  # Prompt user for input
discount_percentage = float(input("Enter the discount percentage: "))  # Prompt user for input

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percentage)
print("Final price:", final_price)