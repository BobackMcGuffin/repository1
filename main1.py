running = True

while running:
    name = input('Enter your name: ')
    print('Your name is', name, ', correct?')

    ans = input('Yes or No?: ')

    if ans == 'Yes':
        running = False
        print('Good')
        continue

    if ans == 'No':
        print('Then what is your name?', end=' ')
        realname = input('Enter it here: ')
        if realname == name:
            print('Don\' fuck with me')
            continue
        else:
            running = False
            print('So your name is', realname, '. Hello', realname)
            continue
    else:
        print('Ok, whatever, we\'ll just go with', name)
        continue

game = True
while game:
    print('Are you ready to begin?')
    ans1 = input('Yes or No?: ')
    if ans1 == 'Yes':
        print('Then let\'s go!')
    else:
        print('Why are you even here?')

    print('Question One: What is two plus two?')
    question1 = True

    while question1:
        ans2 = input('Answer: ')
        if ans2 == '4':
            print('Correct!')
            break
        else:
            print('Try again!')

    print('Question two: You enter a room, and see two doors, which do you take?')
    print('Do you take the Left door, or the Right door?')
    question2 = True
    while question2:
        ans3 = input('Left or Right: ')
        if ans3 == 'Left':
            print('You chose the', ans3, 'door.')
            break
        if ans3 == 'Right':
            print('You chose the', ans3, 'door.')
            break
        else:
            print('Make sure you capitalize')

    if ans3 == 'Right':
        print('You enter the Right room.')
        print('As you open the door, an evil monkey jumps on your face and chews out your eyeballs. I\'m sorry, but you are dead.')
        playagain = input('Play again? Yes or No: ')
        if playagain == 'Yes':
            running = True

        if playagain != 'Yes':
            game = False
            print('Until Next time!')

    if ans3 == 'Left':
        print('You Enter the Left room.')
        print('Inside you find all the riches of Scotland. Congratulations!')
        print('Now you have a choice, would you like to return home with your riches, or continue to the next room?')
        ans4 = input('Return or Continue?: ')
        if ans4 == 'Continue':
            print('You enter the next room, and an evil monkey instantly attacks you, chewing out your eyeballs. You die.')
            playagain = input('Play again? Yes or No: ')
            if playagain == 'Yes':
                running = True

            if playagain != 'Yes':
                game = False
                print('Until Next time!')

        if ans4 == 'Return':
            print('You have escaped with all the riches of Scotland, congratulations!')
            playagain = input('Play again? Yes or No: ')
            if playagain == 'Yes':
                running = True

            if playagain != 'Yes':
                game = False
                print('Until Next time!')
