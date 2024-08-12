print('Welcome to the quiz!')

# Initialize score
score = 0

# Ask the first question
a1 = input('What is the capital city of France? ').strip().lower()
if a1 == 'paris':
    score += 1
    # Ask the second question if the first one is correct
    a2 = input('What is the chemical symbol for the element Gold? ').strip().upper()
    if a2 == 'AU':
        score += 1
        # Ask the third question if the second one is correct
        a3 = input('Who was the first President of the United States? ').strip()
        if a3 == 'George Washington':
            score += 1
            # Ask the fourth question if the third one is correct
            a4 = input('Who wrote the play "Romeo and Juliet"? ').strip().lower()
            if a4 == 'william shakespeare' or a4 == 'shakespeare':
                score += 1
                # Ask the fifth question if the fourth one is correct
                a5 = input('What is the value of π (pi) up to two decimal places? ').strip()
                if a5 == '3.14':
                    score += 1
                else:
                    print('Incorrect. The correct answer is 3.14.')
            else:
                print('Incorrect. The correct answer is William Shakespeare.')
        else:
            print('Incorrect. The correct answer is George Washington.')
    else:
        print('Incorrect. The correct answer is AU.')
else:
    print('Incorrect. The correct answer is Paris.')

# Print the final score
print('Congratulations! You scored', score, 'out of 5.')
