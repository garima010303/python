import random

print("Are you a computer or Human being?")
a = input("Press C for Computer and press H for human being: ")
products = " "

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

elif(a == "H"):
    name = input("Enter your name: ")
    print(f"Welcome, {name}.")
    product = input("What do you want to buy?")
    products += product + " "
    item_list = ["DairyMilk", "Kitkat", "Butterscotch",
                 "Chocolate", "SilkOreo", "Kurkure", "Unclechips", "Brownies"]
    done = " "
    while(product != "done"):

        if product in item_list:
            print(f"{product} is added to list.")
            product = input("What do you want to buy next?")
            products += product + " "
            print(f"Your final products that you want to buy are: {products}")
        else:
            print("Sorry! The item is not available")
            anything = input("Any other item that you want to buy? ")

else:
    print: "Invalid user, please enter C for Computer and H for human being: "

print("Thank you! Have a good day.\nHope to see you next time!")
