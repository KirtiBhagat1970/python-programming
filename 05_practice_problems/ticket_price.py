age=int(input("enter a age:"))
price=int(input("enter a price:"))
discount=price*10/price
tprice=price-discount
if age<12:
    
    print("ticket price:",tprice)
elif age>12:
    price=price-discount
    print("ticket price:",tprice)
