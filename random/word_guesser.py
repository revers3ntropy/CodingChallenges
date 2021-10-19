print('Welcome to guess the word game')

secret_word = input('player 1, please enter the secret word: ')

guessed = False

guesses = 0

while not guessed:
    print('player two please enter a letter')
    guess = input()

    guess = guess[0]

    if guess in secret_word:

        count = 0
        done = False

        while not done:
            secret_word = secret_word.replace(guess, '', 1)
            count += 1

            if guess not in secret_word:
                done = True
        print('That letter appears in the secret word ' + str(count) + ' times')

        if len(secret_word) <= 0:
               guessed = True
        
    else:
        print('That letter doesn\'t appear in the secret word')

    guesses += 1;

print('Player two wins in ' + str(guesses) + ' rounds!')

        
