import random

secretNumber = random.randint(1,20)
print("Between 1 and 20")

for guessTaken in range(1,6):
    print('Guess number ' + str(guessTaken))
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else: 
        break 

if guess == secretNumber:
    print('Correct answer in ' + str(guessTaken) + ' attempts')
else:
    print('The actual number is ' + str(secretNumber))
 