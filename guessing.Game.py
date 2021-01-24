from random import randint 

secret_num = randint(1,5) 

while True: 

    guess = int(input('Guess the secret number: ')) 

    if secret_num == guess: 

        print("Right guess!") 

        break 

print('You finally got it!') 
