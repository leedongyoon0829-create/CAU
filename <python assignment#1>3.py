import random
answer=random.randint(1,100)
print("Guess the number between 1 and 100!")
count=0
while True:
    guess=int(input("Enter your guess: "))
    count+=1
    if guess==answer:
        print(f"Congrats! You guessed it in {count} tries!")
        break;
    elif guess>answer:
        print("too high")
    else:
        print("too low")
