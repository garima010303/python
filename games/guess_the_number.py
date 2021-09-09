import random
rn = random.randint(1,100)
print(rn)
user_number = None
guesses = 0

while(user_number != rn):
    user_number = int(input("Guess the number: "))
    if(user_number==rn):
        print("Congratulations! You guessed it right!")
    elif(user_number < rn):
        print("Bad luck! please try a higher number")
    else:
        print("Bad luck! please try a lower number")
    guesses+= 1

print(f"You guessed the correct number in {guesses} guesses")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!GAME ENDS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
