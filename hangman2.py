import random

play = 'true'

def createBlank(word):
    for c in word:
        blank.append('_')

def fill(blank, letter, word):
    global score
    count = 0
    for c in word:
        if c == letter :
            blank[count] = letter
            score += 1
        count += 1

while play == 'true' :
    words_easy = ['apple', 'banana', 'mango', 'cheese', 'cat', 'mouse']
    words_hard = ['christmas', 'halloween']

    used_letters = []
    blank = []
    word = ''
    
    lives = 14
    goal = 0
    score = 0

    print('==================================================================')
    print('                           Hangman ')
    dif = input('Please select a difficulty (1)Easy, or (2) Hard')
    
    if dif == '1' :
        print('Difficulty: Easy')
        num = random.randint(0, len(words_easy)-1)
        word = words_easy[num]
    else :
        print('Difficulty: Hard')
        num = random.randint(0, len(words_hard)-1)
        word = words_hard[num]
    goal = len(word)
    createBlank(word)
    
    while score != goal :
        print(f"Your word is {blank}")
        letter = input('Please select a letter').lower()
        
        if letter in used_letters :
            print('You have already used that letter')
        elif lives == 0:
            print('Out of lives, you lose :(')
            score = goal
            
        else:
            if letter in word :
                count = 0
                for c in word:
                    if c == letter :
                        blank[count] = letter
                        score += 1
                    count += 1
                print('correct')
                if score == goal :
                   print('You Win!')
                   again = input('Play again? y/n')
                   if again.lower() == 'n' :
                       play = 'false'
            else:
                print('incorrect')
                lives -= 1
                print(lives)
                
    
