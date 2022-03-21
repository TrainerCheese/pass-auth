print('Welcome to this password authectication and manager program. This is developed only for Windows PCs.')

reguserName = input('Enter your username: ')
regpassWord = input('Enter your password: ')
regrePass = input('Re-Enter your password: ')
if regrePass == regpassWord:
    print('Created a account successfully!')
    print('Login')
    loguserName = input('Enter your username: ')
    if loguserName == reguserName:
        logpassWord = input('Enter your password: ')
        if logpassWord == regrePass:
            print('Logged in successfully!')
        else:
            print('Login unsuccessfull. Invalid username or password, Try again')
    else:
        print('Invalid username or password, try again.')
else:
    print('Wrong password try again')
