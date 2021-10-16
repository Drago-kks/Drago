print("\033[96m HELLO")
c = input("\033[93m WHAT IS YOUR NAME = ")
print("\033[96m HI " + c)
x = input("\033[93m  HOW OLD ARE YOU " + c + " = ")
n = int(x)
if (n > 10):
    print("\033[96m OK " + c)
    print("\033[92m NOW TYPE 'password crack'")
if (n < 10):
    print("\033[93m ksk")
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "password crack":
        print('''\033[96m

         ###        ###
         ###        ###
         ###        ###
    ########################
    ########################
         ###    @   ###
    ########################
    ########################
         ###        ###
         ###        ###
         ###        ###


                  CHOSE OPTION
        ________________________________
        1     =  start password cracking
        2     =  exit           ''')

    elif command == "1":
        # importing random
        from random import *

        # taking input from user
        user_pass = input("\033[93m Enter your password = ")

        # storing alphabet letter to use thm to crack password
        password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                    'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z', 'y',
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C',
                    'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P',
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z', 'Y', '!', '@', '#',
                    '$', '%', '^', '^^', '&', '*', '(', ')', '_', '-', '+', '=', '.',
                    '>', '<', ',', '?', '/', ':', ';', '|', '[', ']', '{', '}',
                    ' '' ', ' "" ', '+', '`', '``', '~', '~~']

        # initializing an empty string
        guess = ""

        # using while loop to generate many passwords untill one of
        # them does not matches user_pass
        while (guess != user_pass):
            guess = ""
            # generating random passwords using for loop
            for letter in range(len(user_pass)):
                guess_letter = password[randint(0, 96)]
                guess = str(guess_letter) + str(guess)
            # printing guessed passwords
            print("\033[92m" + guess)

        # printing the matched password
        print("\033[93m Your password is", guess)
        print('''\033[96m


                           CHOCE option
             _______________________________________
             1          =   password cracking againg
             2          =   exit         ''')
    elif command == "2":
        print("BYE "+c)
