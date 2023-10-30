from pickle import FALSE


user_input = ""
started = False
stopped = True
print("THIS IS THE CAR GAME! IF YOU KNOW THE COMMANDS THEN START PLAYING, IF YOU NEED HELP TYPE 'HELP'")
while user_input != "quit":
    user_input = input("> ").lower()

    if user_input == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - exit the program")

    elif user_input == "start":
        if started:
            print("ITS ALREADY STARTED")
        else:
            print("VROOM... the car has started")
            started = True
            stopped = False
            
    elif user_input == "stop":
        if stopped:
          print("ITS ALREADY STOPPED")
        else:
            print("SSKRRRRRRRRRRT... the car has stopped!")
            stopped = True
            started = False

    elif user_input != "start" and "stop":
        if user_input == "quit":
            break
        else:
            print("I dont understand that")