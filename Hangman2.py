import random
name = input("What is your name? ")
list1=['python','heart','read']
list2=['It is a programming language:p_t__n','It is the main part of the body:h_a_t','It is the word we use when there is a exams: _e_d']
word = random.choice(list1)
n=list1.index(word)
print("Good Luck ! ", name)
if word in list1:
    print("Guess the characters") 
    print("the hint of the word is:",list2[n])
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:  
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")
