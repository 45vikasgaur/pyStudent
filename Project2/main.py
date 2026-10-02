import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a number between 1 to 100:"))
    if(a > n):
        print("Lower number please!")
    elif(a < n):
        print("Higher number please!") 
        guesses += 1
    
    
print(f"Congratulations! You guessed the number in {guesses} guesses.")