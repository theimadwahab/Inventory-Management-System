products = []

class User:
    def show_product(self):
        if not products:
            print("No products available.")
            return

        print("Available products:")
        for product in products:
            print(f"Name: {product['name']}")
            print(f"Quantity: {product['quantity']}")
            print(f"Price: {product['price']:.2f}/{product['name']}")
            print()

    def buy_product(self):
        product_name = input("Enter the name of the product: ").upper()
        existing_product = next((product for product in products if product['name'] == product_name), None)

        if existing_product:
            buy_quantity = int(input("Enter quantity to buy: "))

            if buy_quantity <= existing_product['quantity']:
                existing_product['quantity'] -= buy_quantity
                print(f"You have bought {buy_quantity} of {product_name}.")
            else:
                print("Insufficient quantity available.")
        else:
            print("Product not found.")


class Admin(User):

    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):
        try:
            select_opt = int(input("1: For Admin\n2: For User\nSelect option: "))
            if select_opt == 1:
                if self.login():
                    self.admin_menu()
            elif select_opt == 2:
                self.user_menu()
            else:
                print("Please select a valid option.")
                self.menu()
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.menu()

    def admin_menu(self):
        self.trash_hold()
        try:
            select_opt = int(input("1: Add Product\n2: Delete Product\n3: Edit Price\nSelect option: "))
            if select_opt == 1:
                self.add_product()
            elif select_opt == 2:
                self.delete_product()
            elif select_opt == 3:
                self.edit_price()
            else:
                print("Invalid option. Returning to admin menu.")
                self.admin_menu()
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.admin_menu()

    def user_menu(self):
        try:
            select_opt = int(input("1: Show Products\n2: Buy Products\nSelect option: "))
            if select_opt == 1:
                self.show_product()
            elif select_opt == 2:
                self.buy_product()
            else:
                print("Invalid option. Returning to user menu.")
                self.user_menu()
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.user_menu()
    def login(self):
        name_pass = {"saqib": 333, "sadaqat": 555, "waqas": 777, "annas": 999}

        name = input("Enter your name: ").lower()
        try:
            password = int(input("Enter your password: "))
        except ValueError:
            print("Password must be a number.")
            return False

        if name in name_pass and name_pass[name] == password:
            print("Welcome!")
            return True
        else:
            print("Invalid credentials.")
            return False

    def trash_hold(self):
        low_stock_products = [product for product in products if product['quantity'] <= 10]

        if low_stock_products:
            print("The following products are low in quantity and need restocking:")
            for product in low_stock_products:
                print(f"{product['name']}: Quantity is {product['quantity']}")
            print(f"\nTotal products needing restock: {len(low_stock_products)}")
        else:
            print("All products are sufficiently stocked.")


    def add_product(self):
        name = input("Enter product name: ").upper()
        try:
            quantity = int(input("Enter quantity to add: "))
            price = float(input("Enter price: "))
        except ValueError:
            print("Quantity must be an integer and price a number.")
            return

        existing_product = next((product for product in products if product['name'] == name), None)

        if existing_product:
            existing_product['quantity'] += quantity
            print(f"Updated quantity for {name}: {existing_product['quantity']}")
        else:
            new_product = {
                "name": name,
                "quantity": quantity,
                "price": price
            }
            products.append(new_product)
            print(f"\"{quantity}\" {name} (ID: {len(products)}) has been added.")

    def delete_product(self):
        name = input("Enter the name of the product to delete: ").upper()
        existing_product = next((product for product in products if product['name'] == name), None)

        if existing_product:
            products.remove(existing_product)
            print(f"Product {name} has been successfully deleted.")
        else:
            print("The product does not exist.")

    def edit_price(self):
        name = input("Enter the name of the product to edit: ").upper()
        existing_product = next((product for product in products if product['name'] == name), None)

        if existing_product:
            try:
                new_price = float(input("Enter the new price: "))
                existing_product['price'] = new_price
                print(f"Price for {name} successfully updated to {new_price:.2f} ")
            except ValueError:
                print("Price must be a number.")
        else:
            print("The product does not exist.")


admin1=Admin()