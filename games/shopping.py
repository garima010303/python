import random

print("Are you a computer or Human being?")
a = input("Press C for Computer and press H for human being: ")
if(a == "C"):
    print("Choose items that you want to buy: ")  # by random module

    item_list = ["DairyMilk", "Kitkat", "Butterscotch", "Chocolate",
                 "SilkOreo", "Kurkure", "Unclechips", "Brownies", "done"]
    product = random.choice(item_list)
    while(product != 'done'):
        print(product)
        product = random.choice(item_list)
        item_list = ["DairyMilk", "Kitkat", "Butterscotch", "Chocolate",
                     "SilkOreo", "Kurkure", "Unclechips", "Brownies", "done"]
        if(item_list == 'done'):
            print("Thank you! Have a good day.")


else:
    name = input("Enter your name: ")
    print(f"Welcome, {name}.")
    product = input("What do you want to buy?")
    item_list = ["DairyMilk", "Kitkat", "Butterscotch",
                 "Chocolate", "SilkOreo", "Kurkure", "Unclechips", "Brownies"]
    done = "done"
    while(product != done):

        if product in item_list:
            print(f"{product} is added to list.")
            product = input("What do you want to buy?")
        else:
            print("Sorry! The item is not available")
            product = input("Any other item that you want to buy? ")
        print(product)
print("Thank you! Have a good day.")
