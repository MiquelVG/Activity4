import os
import sys

################################### GLEN'S STORY ###################################

########################## PROGRAM END, CLEAR and CHOICES ##########################

def you_lose_end():#YOU LOSE
    print()
    print("-------------")
    print("--GAME OVER--")
    print("--YOU  LOSE--")
    print("-------------")
    print()
    input("Press any key to exit ")
    print("Exiting the program...")
    sys.exit()

def you_win_end():#YOU WIN
    print()
    print("-------------")
    print("--GAME OVER--")
    print("---YOU WIN---")
    print("-------------")
    print()
    input("Press any key to exit ")
    print("Exiting the program...")
    sys.exit()


def get_user_choice2():#2 Choices
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_user_choice3():#3 Choices
    while True:
        choice = input("Enter your choice (1, 2 or 3): ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


########################################## STORIES ##########################################
              
def up_ladder(): #Up Ladder
    clear_screen()
    print("You climb for what seems like an eternity but finally end up in a room with a swimming pool.")
    print("What do you do next?")
    print()
    print("1. Take a swim.")
    print("2. Find another way out.")
    print()

def down_ladder(): #Down Ladder
    clear_screen()
    print("A hatch suddenly closes behind you! You try to open it but no use, so you begin to descend the ladder. You start to notice you can't breath and you feel an immense suction force beneath you.")
    print("You can't hold on any longer and let go.... Barely conscious, you realise you have been ejected into the infinite vacuum of space....")
    print()
    input("Press any key to continue...")
    you_lose_end()

def turn_back(): #Turn Back
    clear_screen()
    print("You head back down the corridor and see an elevator")
    print("It has 2 floors but the names are too difficult to make out.")
    print("Which floor?")
    print()
    print("1. ` s  ' , ` n . '")
    print("2. E,.c; P.'s`'.r,")
    print()

def acid_pool_coutcome(): #Acid Pool Outcome
    clear_screen()
    print("You do your best swan dive, at least a 7 out of 10 you think to yourself.")
    print("Unfortunately for you, it is not a pool. It is infact a rather large deposit of a highly acidic acid!")
    print()
    input("Press any key to continue...")
    you_lose_end()

def turn_back_outcome2(): #Turn Back Outcome 2
    clear_screen()
    print("You notice after you have pressed the button that there is a broken key next to it.")
    print("You look closer at the floor name on the button panel and realise it was just a bit dirty, so you rub the dirt away.")
    print()
    print("Ej,ct Pri,oners.")
    print("WARN`NG: Turn k.y and leave e;evator.")
    print()
    print("If you don't already know, you have ejected yourself from the spaceship. Ahh the irony!")
    print()
    input("Press any key to continue...")
    you_lose_end()

def elevator_floors(): #Elevator Floors
    clear_screen()
    print("After exploring a bit of the room, you find an elevator.")
    print("You see that there are 3 extra floors that you can go to.")
    print("Unfortunately the names are quite faded and hard to make out.")
    print("What do you press?")
    print()
    print("1. Syst `o vtr ls.")
    print("2. -sca e P d^.")
    print("3. P`is n C l`s.")
    print()

def elevator_floors_outcome3(): #Elevator_Floors_Outcome3
    clear_screen()
    print("The elevator starts going down but very slowly.")
    print("You get the feeling that this may have been a terrible choice but there is no turning back.")
    print("The doors open and you are greeted with several guards standing outside.")
    print("It turns out that the floor on the elevator button panel said 'Prison Cells'!!!.")
    print()
    input("Press any key to continue...")
    you_lose_end()


def control_room(): #Control Room
    clear_screen()
    print("You have entered the system control room.")
    print("The pilot of the spaceship is manning the controls and has not seen you yet.")
    print("What do you do next?")
    print()
    print("1. Charge at the pilot to take him out.")
    print("2. Sneak up on him")
    print("3. Press the big red button...")
    print()

def control_room_outcome1(): #Control Room Outcome1
    clear_screen()
    print("You charge at the pilot but he hears you coming.")
    print("He turns around and presses a button on his belt. You fall to the ground instantly in pain.")
    print("Unfortunately you have been wearing an electric prison collar.")
    print()
    input("Press any key to continue...")
    you_lose_end()

def control_room_outcome2(): #Control Room Outcome2
    clear_screen()
    print("You sneak like a serpent up on the pilot and he has no clue you are there.")
    print("Once close enough you lunge and grab hold of him in a rear hold choke.")
    print("You demand him to open a space pod and you escape in the pod.")
    print()
    input("Press any key to continue...")
    you_win_end()

def control_room_outcome3(): #Control Room Outcome3
    clear_screen()
    print("You see a big red button and can't help yourself.")
    print("You push the big red button and the spaceship explodes spectacularly!")
    print()
    input("Press any key to continue...")
    you_lose_end()

def escape_pods(): #Escape Pods
    clear_screen()
    print("What a stroke of luck! You have found the room of the spaceships escape pods.")
    print("There are a 3 pods to enter.")
    print("Which one will you take to escape the ship?")
    print()
    print("1. Pod 16")
    print("2. Pod 17")
    print("3. Pod 18")
    print()

def escape_pod_outcome1(): #Escape Pod Outcome1
    clear_screen()
    print("You open Pod 16 and and go in.")
    print("The controls are clearly labeled and you've had some flying experience before.")
    print("You eject in the pod and escape the spaceship!!")
    print()
    input("Press any key to continue...")
    you_win_end()

def escape_pod_outcome2(): #Escape Pod Outcome2
    clear_screen()
    print("You open Pod 17 but find there is an android (robot) inside.")
    print("The android immediately captures you and turns you over to the spaceship crew.")
    print("Your punishment will be even harsher for your troubles...")
    print()
    input("Press any key to continue...")
    you_lose_end()

def escape_pod_outcome3(): #Escape Pod Outcome3
    clear_screen()
    print("You open Pod 18 and go inside.")
    print("It seems to be quite and old pod and the controls don't seem to be very clear.")
    print("You press what you think is the iginition but unfortunately you have activated the stasis system.")
    print("The stasis system puts the user to sleep for on long journeys across the galaxy.")
    print("Unfortunately you don't have time on your hands and you are eventually caught by the spaceship crew.")
    print()
    input("Press any key to continue...")
    you_lose_end()


########################################## GLEN MAIN ##########################################

def glen_main():

    clear_screen()
    print("You go down a narrow dark corridor and arrive to ladder.")
    print("There are holes in both the ceiling and the floor where the ladder passes through.")
    print("What do you do?")
    print()
    print("1-Climb up the ladder.")
    print("2-Climb down the ladder.")
    print("3-Turn back.")

    choice = get_user_choice3()

    if choice == '1': #Up the ladder
        up_ladder()
        choice = get_user_choice2()
        if choice == '1': 
            acid_pool_coutcome()#YOU LOSE
        else:
            elevator_floors()
            choice = get_user_choice3()
            if choice == '1':
                control_room() #Control Room
                choice = get_user_choice3()
                if choice == '1':
                    control_room_outcome1()#YOU LOSE
                elif choice == '2':
                    control_room_outcome2()#YOU WIN
                else:
                    control_room_outcome3()#YOU LOSE
            elif choice == '2':
                escape_pods()
                choice = get_user_choice3()
                if choice == '1':
                    escape_pod_outcome1()#YOU WIN
                elif choice == '2':
                    escape_pod_outcome2()#YOU LOSE
                else:
                    escape_pod_outcome3()#YOU LOSE
            else:
                elevator_floors_outcome3()#YOU LOSE
    elif choice == '2': #Down the ladder
        down_ladder() #YOU LOSE
    else: #Turn back
        turn_back()
        choice = get_user_choice2()
        if choice == '1':
            control_room()
            choice = get_user_choice3()
            if choice == '1':
                control_room_outcome1() #YOU LOSE
            elif choice == '2':
                control_room_outcome2() #YOU WIN
            else:
                control_room_outcome3() #YOU LOSE                
        else:
            turn_back_outcome2()#YOU LOSE 

########################################## END GLEN ##########################################

print("You are a prisoner that has been held captive on a Spaceship for 6 months.\n Now it's your time to escape. A guard that you bribed will come at night time to open your cell.")
print("The guard came and opened your cell, where will you go?")
print("1-Go left")
print("2-Go right")
print("3-Go straight")
option = int(input())
while option < 1 and option > 3:
    print("Not valid option. Try again: ")
    option = int(input())
if option == 1:
    print("You arrive at the door leading to the room where the escape pods are located, but the electronic door is closed.")
    print("What do you do?")
    print("1-Try to hack the door from the control panel next to it.")
    print("2-Wait for someone to open the door.")
    print("3-Go in another direction.")
    option = int(input())
    while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
        print("Not valid option. Try again: ")
        option = int(input())
    if option == 1:#If the user chooses this option, this will be executed.
        os.system("cls")
        print("You fail to hack the panel and an alarm sounds.")
        print("What do you do?")
        print("1-Persist and try to hack the panel before the guards arrive.")
        print("2-Hide in a hiding spot.")
        print("3-Run away.")
        option = int(input())
        while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
            print("Not valid option. Try again: ")
            option = int(input())
        if option == 1:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("You manage to open the door just as the guards arrive, and they are armed!")
            print("You must choose quickly, which escape pod do you pick?")
            print("1-The first.")
            print("2-The second.")
            print("3-The third.")
            option = int(input())
            while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You went as fast as you could, but you didn't realize that the escape pod was under repair.")
                print("As a result, the escape pod doesn't start, and the guards capture you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 2:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You were fast enough and realized that the first escape pod was under repair.")
                print("The second escape pod starts, and you manage to escape.")
                print("-------------")
                print("--GAME OVER--")
                print("---YOU WIN---")
                print("-------------")
            elif option == 3:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You weren't fast enough, the third capsule was too far away.")
                print("One of the guards' shots hits you, and they manage to capture you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
        elif option == 2:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("A guard opens the door to see if there's anyone.")
            print("What do you do?")
            print("1-Run towards the escape pod room.")
            print("2-Continue hiding.")
            print("3-Grab a guard as a hostage.")
            option = int(input())
            while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You run as fast as you can, but the guards are faster and capture you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 2:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You continue hiding, but the guards begin to search the area and eventually find and capture you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 3:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You wait for the perfect moment to leave your hiding spot and catch a guard off guard.")
                print("You use him as a hostage and escape in one of the capsules.")
                print("-------------")
                print("--GAME OVER--")
                print("---YOU WIN---")
                print("-------------")
        elif option == 3:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("You try to run away, but along the way you encounter some guards who capture you.")
            print("-------------")
            print("--GAME OVER--")
            print("--YOU  LOSE--")
            print("-------------")
    if option == 2:#If the user chooses this option, this will be executed.
        os.system("cls")
        print("You've been waiting for a long time, but no one opens the door, although that makes sense, they're escape pods, only used in emergencies.")
        print("What do you do?")
        print("1-Continue waiting.")
        print("2-Go in another direction.")
        print("3-Trigger an accident.")
        option = int(input())
        while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
            print("Not valid option. Try again: ")
            option = int(input())
        if option == 1:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("You keep waiting until suddenly an alarm sounds and you hear a voice saying, 'He has escaped.'")
            print("What do you do?")
            print("1-Try to hack the door from the control panel next to it.")
            print("2-Hide in a hiding spot and continue waiting.")
            print("3-Blend in with the crowd.")
            option = int(input())
            while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You fail to hack the panel, and the guards capture you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 2:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You continue hiding until they stop searching, and finally, a maintenance worker opens")
                print("the door for inspection, allowing you to escape in an escape pod.")
                print("-------------")
                print("--GAME OVER--")
                print("---YOU WIN---")
                print("-------------")
            elif option == 3:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You blend into the crowd, but since you're wearing prisoner clothes,")
                print("the guards quickly identify you and end up capturing you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
        elif option == 2:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("You go in another direction, but along the way, you encounter some guards who capture you.")
            print("-------------")
            print("--GAME OVER--")
            print("--YOU  LOSE--")
            print("-------------")
        elif option == 3:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("What accident do you think you should provoke?")
            print("1-Start a fire")
            print("2-Make a hole in the spaceship wall.")
            print("3-Trip a waiter.")
            option = int(input())
            while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You provoke a large fire, and even though the ceiling extinguishers quickly put out the fire,")
                print("people get scared and head towards the escape pods, opening the door and allowing you to escape in one of them.")
                print("-------------")
                print("--GAME OVER--")
                print("---YOU WIN---")
                print("-------------")
            elif option == 2:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You head to the engine room and blow up the engine.")
                print("That causes a huge hole that sucks you out into outer space.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 3:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("Why did you do that, you didn't accomplish anything, you just drew attention and the guards captured you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
    if option == 3:#If the user chooses this option, this will be executed.
        os.system("cls")
        print("You decide to go in another direction.")
        print("Where will you go?")
        print("1-Return to the cell.")
        print("2-Go towards the auxiliary spaceship of the spacship.")
        print("3-Go to the bridge to talk to the captain.")
        option = int(input())
        while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
            print("Not valid option. Try again: ")
            option = int(input())
        if option == 1:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("I don't understand why you chose this option, you've locked yourself up again.")
            print("-------------")
            print("--GAME OVER--")
            print("--YOU  LOSE--")
            print("-------------")
        elif option == 2:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("You arrive at the spaceport of the spaceship to board the auxiliary spaceship.")
            print("What do you do?")
            print("1-Try to hack the control panel to board the spaceship and escape.")
            print("2-Convince a pilot that you need them to take you in the spaceship.")
            print("3-Wait for someone to board the spaceship and sneak aboard as a stowaway.")
            option = int(input())
            while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You manage to hack the control panel and board the spaceship while some guards see you and shoot at you.")
                print("Eventually, you manage to escape.")
                print("-------------")
                print("--GAME OVER--")
                print("---YOU WIN---")
                print("-------------")
            elif option == 2:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("The pilot doesn't believe anything you say and realizes you're the prisoner. Then some guards arrive and capture you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 3:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("Time passes, and nobody boards the spaceship until suddenly an alarm sounds, two guards spot you and capture you.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
        elif option == 3:#If the user chooses this option, this will be executed.
            os.system("cls")
            print("You go to the bridge to speak with the captain.")
            print("What do you say to him?")
            print("1-Tell him that it's all a mistake and that you shouldn't be imprisoned.")
            print("2-Confess your deeds and admit you are guilty.")
            print("3-Tell him that you have a witness who can verify that you are not guilty.")
            option = int(input())
            while option < 1 and option > 3:#Use the while loop so that if the user doesn't enter a valid data, the program doesn't crash.
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("The captain doesn't believe you.")
                print("The guards capture you and take you back to the cell.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 2:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You confess your actions, and thanks to that, the guards capture you and take you back to the cell.")
                print("-------------")
                print("--GAME OVER--")
                print("--YOU  LOSE--")
                print("-------------")
            elif option == 3:#If the user chooses this option, this will be executed.
                os.system("cls")
                print("You ask for the guard you had previously bribed to come, and he testifies in your favor, thus securing your release.")
                print("-------------")
                print("--GAME OVER--")
                print("---YOU WIN---")
                print("-------------")
if option == 2:
    glen_main()

if option == 3:
    #First we ask a question.
    print("You arrive to the maintenance room. These are your options:")
    print("1-Check the old Spaceship map on the wall.")
    print("2-Grab a rusty pipe on the floor.")
    print("3-Go further on the maintenance room.")
    option = int(input())
    while option < 1 and option > 3:
        print("Not valid option. Try again: ")
        option = int(input())
        #If the user doesn't enter a valid answer it will keep asking for a valid one.

    #Every option has it's own path.
    if option == 1:
        os.system("cls")
        print("After taking a look to the map you realise that there's an emergency escape ship room.")
        print("That could be your only chance.")
        print("1-Got to the escape pod room.")
        print("2-Not risk it and try to go to the parking station.")
        option = int(input())
        while option < 1 and option > 2:
            print("Not valid option. Try again: ")
            option = int(input())
        if option == 1:
            os.system("cls")
            print("As you approach the room you see two guards patroling the zone. There's only one escape ship left.")
            print("What will you do?")
            print("1-Make a run for it.")
            print("2-Distract the guards.")
            print("3-Wait for the guards to go.")
            option = int(input())
            while option < 1 and option > 3:
                print("Not valid option. Try again: ")
                option = int(input())
                if option == 1:
                    os.system("cls")
                    print("")
                    print("You run as fast as you can towards the escape ship but the guards catch you before you could have entered it.")
                    print("---THE END---")
                if option == 2:
                    os.system("cls")
                    print("You grab a tool you had nearby and throw it, the guards go to check the sound.")
                    print("You did it! You got into the escape ship and returned home")
                    print("---THE END---")
                else:
                    os.system("cls")
                    print("You wait for the guards to leave.")
                    print("After some time you fall asleep and get caught.")
                    print("---THE END---")
        else:
            os.system("cls")
            print("You cautiously get to the parking station where you fin a lot of parked small Spaceships.")
            print("You see a set of keys and decide to take them.")
            print("1-Try to steal a Spaceship from the principal door.")
            print("2-Try to steal a Spaceship from the back door.")
            print("3-Try to force open a Spaceship.")
            option = int(input())
            while option < 1 and option > 3:
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:
                os.system("cls")
                print("The keys weren't for the principal door and you set off the alarm. The guards caught you.")
                print("---The End---")
            if option == 2:
                os.system("cls")
                print("You manage to open the back door of the Spaceship.")
                print("Once you start it you finally get out.")
                print("---The End---")
            else:
                os.system("cls")
                print("You try to force open a Spaceship and it sets off the alarm.")
                print("You get caught.")
                print("---The End---")
    if option == 2:
        os.system("cls")
        print("Maybe the pipe will be usefull.")
        print("Suddenly you hear footsepts. What will you do?")
        print("1-Hide.")
        print("2-Wait to atack.")
        print("3-Go towards the footseps")
        option = int(input())
        while option < 1 and option > 3:
            print("Not valid option. Try again: ")
            option = int(input())
        if option == 1:
            os.system("cls")
            print("You don't hide fast enough and a guard spots and catches you.")
            print("---The End---")
        if option == 2:
            os.system("cls")
            print("You try to attack the guard that was coming but he fires his weapon and kills you.")
            print("---The End---")
        else:
            os.system("cls")
            print("You go twoards the footseps without knowing that it's a guard. He catches you.")
            print("---The End---")
            
    else:
        os.system("cls")
        print("After exploring a bit you get to a dark room were a beast is kept in a big cell.")
        print("It asks you to free him and it will help you.")
        print("1-Free it.")
        print("2-Don't free it")
        option = int(input())
        while option < 1 and option > 2:
            print("Not valid option. Try again: ")
            option = int(input())
        if option == 1:
            os.system("cls")
            print("You free the beast and it kills everyone on the ship except you.")
            print("You manage to escape.")
            print("---The End---")
        else:
            os.system("cls")
            print("You refuse to free the beast but it's too late. A few guards heard you and caught you.")
            print("---The End---")