import random

chooseOpponent = input("Do you want to play with computer? yes/no:")
while chooseOpponent != "yes" and chooseOpponent != "no":
       chooseOpponent = input("Do you want to play with computer? yes/no:")

if chooseOpponent == "yes":
       letters = random.sample('0123456789', 3)
       if letters[0] == '0':
           letters.reverse()
       secretNumber = ''.join(letters)

elif chooseOpponent == "no":
       secretNumber = input("let your friend enter a 3 digit secret number")

       while len(secretNumber) != 3 or secretNumber.isdigit() == False:
       
              secretNumber = input("Please re-enter secret Number, secret number must be 3 digits and not text")

print("Good! Secret number stored correctly")
print("Your turn!")
print(' "pico" when your guess has a correct digit in the wrong position.')
print(' "fermi" when your guess has a correct digit in the correct place.')
print(' "bagels" if your guess has no correct digits.')
print("You have 10 tries to guess the secret number")


tries = 1
while True:
       
    
    guess = input("Guess the secret answer")
    
    if len(guess) != 3 or guess.isdigit() == False:
        print("Try again, number must be 3digits")
        

    list=[]
    
    for i in range(3):
        if guess[i] == secretNumber[i]:
            list.append('fermi')
        elif guess[i] in secretNumber:
            list.append('pico')

    random.shuffle(list)
    if len(list) == 0:
        print('bagels')
    else:
        print(list)

    
    print("you have' ",10-tries," ' trials left")
    tries += 1

    if guess == secretNumber:
        print('Good your last guess is Correct! You got it! secret number is ',secretNumber)
        break

    if tries > 10:
        print("You are out of trials. The answer is ", secretNumber)
        break

    

    
    
    


    
