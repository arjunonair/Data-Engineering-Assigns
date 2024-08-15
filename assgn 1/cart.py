from DB import *

def display_cart():
    if len(cart) == 0:
        print("Cart is empty !")
    else:
        for product in cart:
            print(f"SessionID : {product['SessionID']}\tProductID : {product['ProductID']}\tQuantity : {product['quantity']}")

def add_to_cart(sessionID):
    SessionID = sessionID
    ProductID = input('Product Id : ')
    Quantity = int(input('Enter the quantity : '))
    for produt in cart:
        if produt['ProductID'] == ProductID:
            produt['quantity'] += Quantity
            return
    cart.append({'SessionID':SessionID,'ProductID':ProductID,'quantity':Quantity})

def delete_from_cart(sessionID):
    SessionID = sessionID
    ProductID = input('Product Id : ')
    count = 0
    for product in cart:
        if product['SessionID']==SessionID and product['ProductID']==ProductID:
            cart.remove(product)
            print(f"Product {product['ProductID']} is removed from the cart")
        count += 1
    if count == len(product):
        print('\nInvalid id , please check it!')