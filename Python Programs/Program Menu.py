# Description: This program is a menu that allows the user to select from 6 different options containing the completed code for the Midterm Sprint, aswell as an exit option. The program will loop until the user selects the exit option.
# Author: Brandon Maloney & Group 6/SD 14
# Date(s): February 18, 2025 - Febuary 18, 2025

# Define required libraries.
import os

# Define program constants.

# Define program functions.

# Main program starts here.

while True:

    # Display the main menu.
    os.system("cls" if os.name == "nt" else "clear")
    print(" --------------------------------")
    print(" |  Midterm Sprint - Main Menu  |")
    print(" --------------------------------")
    while True:
        allowed_char = set("1234567890")
        print(" Please select from the following options:")
        print(" 1. Complete a travel claim.")
        print(" 2. Fun interview questions.")    
        print(" 3. Cool stuff with strings and dates.")
        print(" 4. A little bit of everything.")
        print(" 5. Something old, something new.")
        print(" 6. Exit program.")
        print(("""     
        "Sweet"                     )      ((     (
            -Brandon               (        ))     )
                            )       )      //     (
                       _   (        __    (     ~->>
                ,-----' |__,_~~___<'__`)-~__--__-~->> <
                | //  : | \\_ \\~_\\-\\__\\-\\_\\ '\\>-  >
                | //  : |- \\_ \\ -\\_\\ -\\ \\ \\ ~\\_  \\ ->> - ,  >>
                | //  : |_~_\\ -\\__\\ \\~'\\ \\ \\, \\__ . -<-  >>
                `-----._|--.----`-- - /~ -- ` --~> >
                 _/___\\_    //)_`//  | ||]
           _____[_______]_[~~-_ (.L_ / / |
          [____________________]' `\\/   /
            ||| /          |||  ,___,'./
            ||| \\          |||,'______|
            ||| /          /|| I==||
            ||| \\      __ /_||  __||__
-------------||-/------`-._/||-o--o---o--------------------------------
~~~~~~~~~~~~~~~'"""))
        # Gather user inputs.
        Menu = input("Enter your selection (1-6): ")
        os.system("cls" if os.name == "nt" else "clear")
        if Menu == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print("This is option Complete a travel claim from the menu.")
            print()
            print()
            continue
        elif Menu == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("This is the option Fun interview questions from the menu.")
            print()
            print()
            continue
        elif Menu == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print("This is the option Cool stuff with strings and dates from the menu.")
            print()
            print()
            continue
        elif Menu == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print("This is the option A Little Bit of Everything from the menu.")
            print()
            print()
            continue
        elif Menu == "5":
            os.system("cls" if os.name == "nt" else "clear")
            print("This is the option Something Old, Something New from the menu.")
            print()
            print()
            continue
        elif Menu == "6":
            os.system("cls" if os.name == "nt" else "clear")
            print
            print(('''   ...    *    .   _  .   
*  .  *     .   * (_)   *
  .      |*  ..   *   ..
   .  * \|  *  ___  . . *
*   \/   |/ \/{o,o}     .
  _\_\   |  / /)  )* _/_ *
      \ \| /,--"-"---  ..
_-----`  |(,__,__/__/_ .
       \ ||      ..
        ||| .            *
        |||
        |||
  , -=-~' .-^- _'''))
            print()
            print("Exiting program. Hope you had a great Sprint!")
            break
        elif Menu == "7" or Menu == "8" or Menu == "9" or Menu == "0":
            print()
            print("     Error - Selection must be 1, 2, 3, 4, 5, or 6.")
            print()
        elif Menu == "":
            print()
            print("     Error - Selection must not be blank.")
            print()
        elif set(Menu).issubset(allowed_char) == False:
            print()
            print("     Error - Selection must be numeric only.")
            print()
        else:
            print()
            print("     Error - Selection must be 1, 2, 3, 4, 5, 6.")
            print()
    if Menu == "6":
        break
    else:
        continue

