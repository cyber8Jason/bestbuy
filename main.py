from products import Product
from store import Store

def start(store: Store):
    while True:
        print("\n===== Store Menu =====")
        print("----------------------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number (1-4): ")

        if choice == "1":
            products = store.get_all_products()
            print("\n--- Products Available ---")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.show()}")

        elif choice == "2":
            total = store.get_total_quantity()
            print(f"\nTotal of {total} items in store   ")

        elif choice == "3":
            products = store.get_all_products()
            print("\n--- Products Available for Order ---")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.show()}")

            shopping_list = []
            while True:
                try:
                    product_num = input("\nWhen you want to finish an order, enter empty text."
                                            "\nWhich product # do you want? ")
                    if product_num == "":
                        break
                    product_num = int(product_num)
                    if 1 <= product_num <= len(products):
                        quantity = int(input("What amount do you want? "))
                        shopping_list.append((products[product_num - 1], quantity))
                        print("Product added to list!")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Please enter a valid number.")

            try:
                total_cost = store.order(shopping_list)
                print(f"\nOrder made! Total payment: ${total_cost:.2f}")
            except Exception as e:
                print(f"\nOrder failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = Store(product_list)
    start(best_buy)
