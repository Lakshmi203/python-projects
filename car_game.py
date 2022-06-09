user_input = ''
started = False
while True:
    user_input = input("> ").lower()
    if (user_input == 'help'):
        print('''
start - start the car
stop - car stopped
quit - quit the game
            ''')
    elif (user_input == 'start'):
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif (user_input == 'stop'):
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")
    elif (user_input == 'quit'):
        break

    else:
        print("select valid command")