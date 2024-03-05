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