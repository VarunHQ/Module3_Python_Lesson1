def greet_customer():
    print("Hello! Welcome to our Lemonde Stand!")
    print("We have a variety of refreshing lemonades to choose from made just for you!")

greet_customer()

price_per_cup = float(input("What is the price per cup of the lemonade? (in Dollars!) :"))
cups_sold = int(input("How many cups of lemonade did we sell today? :"))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost  = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("The total cost of lemonade sold is: $", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: $ "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thankyou_message(cups):
    if cups >= 5:
        return "Wow! You have brought a lot of our tasty and refreshing lemonade! Thank you for your kind support!"
    else:
        return "Thank you for your purchase! We hope that you enjoy our tasty and refreshing lemonade!"

closing_message = thankyou_message(cups_sold)

print("")
print(" ===== REFRESHING LEMONADE STAND RECEIPT ===== ")
print("Price per Cup: $ ", price_per_cup)
print("Cups Sold: ", cups_sold)
print("Total Cost: $", rounded_total)
print("Amount Paid: $", amount_paid)
print("Change Due: $", rounded_change)
print(closing_message)
print("=" * 20)