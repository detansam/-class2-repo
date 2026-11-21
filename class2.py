#fullName = "Ayotunde Aladetan"
#car = "honda"

#age = 35
#weight = 54.7   #float
#NightClass = True
#print(fullName , car , age, weight, NightClass)

#print(type(car))

product_name = "Wireless Mouse"
unit_price = 5999.99
stock_quantity = 56
isAvailable = "True"
customer_name = "ayo"
customer_demand = 3
delivery_fee = 1000
total_stock = unit_price * customer_demand + delivery_fee
payment_confirmation_status = "paid"
remaining_stock = stock_quantity - customer_demand
average_cost_per_item = stock_quantity / customer_demand


print(customer_name, "wants to buy", customer_demand, "pieces of", product_name, "out of", stock_quantity, "pieces totalling", total_stock)
print(average_cost_per_item)
print(remaining_stock)
print(payment_confirmation_status)
