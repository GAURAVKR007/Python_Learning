from Shopping.shopping_cart import cart        # Another Way to Import      [from '''''' import * also Works]

# import Shopping.shopping_cart                # I am importing a module shopping_cart from a package name Shopping 

# print(Shopping.shopping_cart.cart("Xbox"))

if __name__ == '__main__':                  # Check the File if the File is main file or not
    print(cart("PlayStation 5"))