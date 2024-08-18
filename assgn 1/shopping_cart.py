import random
from time import sleep

#Logic for user login
def user_login():
    user_name = input("\nEnter your Username : ")
    password = input("Enter your Password : ")

    for user in user_db:
        if user['username'] == user_name and user['password'] == password:
            print('\nLogin successfull as user\n')
            print(f'Hello , {user_name}')
            disply_catalog()
            if not user_interaction(generate_session_id()):
                break
        else:
            print('\nLogin failed!')

#Logic for admin login
def admin_login():
    user_name = input("\nEnter your Username : ")
    password = input("Enter your Password : ")

    for user in admin_db:
        if user['username'] == user_name and user['password'] == password:
            print('\nLogin successfull as admin')
            admin_interaction()
        else:
            print('\nLogin failed!')

#Generates 5 digit session ID
def generate_session_id():
    session_id = random.randint(10000,99999)
    return session_id

#Displays the products
def disply_catalog():
    print('\n--------------------------- PRODUCTS -------------------------------')
    print('''\nID\t\tName\t\tCategory\t\tPrice''')
    print("***\t\t****\t\t*********\t\t*****\n")
    for product in product_catalog:
        print(f'''{product['id']}\t\t{product['name']}\t\t{product['category']}\t\t{product['price']}''')

def user_interaction(sessionID):
    while True:
        print('\n---------------------------------------------------------------------')
        print('''
        1 -> To View the Cart
        2 -> To add to the Cart
        3 -> To delete from the cart
        4 -> To checkout the cart
        5 -> Login as admin    
        6 -> To logout from the system
        ''')
        print('\n---------------------------------------------------------------------')
        ch = input("\nEnter your choice : ")
        if ch == '1':
            display_cart()
        elif ch == '2':
            add_to_cart(sessionID)
        elif ch == '3':
            delete_from_cart(sessionID)
        elif ch == '4':
            checkout()
        elif ch == '5':
            admin_login()
        elif ch == '6':
            print('\nSucessfully logged out as User!\n')
            return False
        else:
            print('\nInvalid Choice. Please choose any other option!')

#Checkout for cart
def checkout():
    if len(cart) == 0:
        print('\nAdd some items to perform checkout!')
        return
    print('Select the payment method : ')
    print('-----------------------------')
    print('''
    1 -> Debit/Credit card
    2 -> UPI
    3 -> Pay on Delevery
    ''')
    payment = int(input('Pay Using : '))

    if payment == 1:
        card_no = input('\nEnter your card No : ')
        print(f'Money debited from your card {'x'*len(card_no)-4}{card_no[-4:]} Happy shopping!')
    elif payment == 2:
        upi_id = input('Enter your UPI ID : ')
        print('Redirecting to the UPI page....')
        sleep(1.4)
        print('Payment successfull.')
    elif payment == 3:
        print('Thanks for shopping with us. Have a nice day :)')
    cart.clear()
    print("\nRedirecting to User dashboard in 3...2...1...")
    sleep(3)

def admin_interaction():
    while True:
        print('\n---------------------------------------------------------------------')
        print('''
        1 -> To add product
        2 -> To update product
        3 -> To delete the product
        4 -> To view the products
        5 -> To logout as Admin
        ''')
        print('\n---------------------------------------------------------------------')
        ch = int(input("\nEnter your choice : "))

        if ch == 1:
            iD = str(int(product_catalog[-1]['id']) + 1)
            name = input('Enter the product name : ')
            category = input("Enter the category : ")
            price = input("Enter the price of the product : ")
            product_catalog.append({'id':iD,'name':name,'category':category,'price':price})
            print(f'\nProduct {name} added to the catalog!')

        elif ch == 2:
            iD = input('Enter the ID of the Product : ')
            name = input('Enter the product name : ')
            category = input("Enter the category : ")
            price = input("Enter the price of the product : ")

            for product in product_catalog:
                if product['id'] == iD:
                    product['name'] = name if name else product['name']
                    product['category'] = category if category else product['category']
                    product['price'] = price if price else product['price']
            print(f'\nProduct {name} has been updated!')

        elif ch == 3:
            iD = input('Enter the Product(ID) to be deleted : ')
            for product in product_catalog:
                if product['id'] == iD:
                    product_catalog.remove(product)  
                    print('\nProduct deleted Sucessfully')
        elif ch == 4:
            disply_catalog()
        elif ch == 5:
            print('\nSucessfully logged out as Admin!\n')
            break
        else:
            print('\nInvalid choice')

print("\n\t\t* WELCOME TO DEMO MARKETPLACE *\n")
print('---------------------------------------------------------------------')

role = input('\nLogin as user or as an admin : ')
if role.lower() == 'user':
    user_login()
elif role.lower() == 'admin':
    admin_login()
else:
    print("Invalid role please login again !")

#Main function
while True:
    print("\n\n-------------------- DEMO MARKETPLACE HOME PAGE ---------------------")
    print('\n---------------------------------------------------------------------')
    print('''
        login -> Login again to the Market
        display -> To display the products
        exit -> To exit from the system
    ''')
    print('\n---------------------------------------------------------------------')
    choice = input('\nEnter your choice : ')
    if choice== 'login':
        role = input('Enter login as user or as an admin : ')
        if role.lower() == 'user':
            user_login()
        elif role.lower() == 'admin':
            admin_login()
        else:
            print("Invalid role please login again !")

    elif choice == 'display':
        disply_catalog()

    elif choice == 'exit':
        print("\nThank you visiting us!\n")
        break
    else:
        print('\nInvalid choice. Try again!')
