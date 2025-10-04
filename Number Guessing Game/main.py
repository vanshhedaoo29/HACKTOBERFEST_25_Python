import random

n = random.randint(1, 100)
a = -1
guesses = 1  

print("=" * 40)
print(" Welcome to the Number Guessing Game ")
print("=" * 40)
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")
print("-" * 40)

while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempt")