age=int(input("enter a age:"))
ticket_price=float(input("enter a ticket price:"))
if age<12:
    discount=ticket_price*10/100
    
else :
    discount=ticket_price*5/100

final_price=ticket_price-discount
print("discount:",discount)
print("final ticket price:",final_price)
    