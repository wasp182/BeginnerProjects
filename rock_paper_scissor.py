import random

def play():
    menu = {
        "rock": "r",
        "paper" : "p",
        "scissor" : "s"
    }
    menu = {
        1 : "r",
        2 : "p",
        3 : "s"
    }
    print("Sno."+" "*2+"choice")
    for items in menu:
        print("{0} ".format(items) +" "*2+":"+" "*2 + " {} ".format(menu[items]))
    inp_choice = ""
    while(inp_choice.casefold() != "q"):
        inp_choice = input("Enter choice as r , p , s .  Press q to quit : ")
        if inp_choice.casefold()!="q":
            comp_choice = menu[random.randint(1,3)]
            if inp_choice == comp_choice :
                print("Draw between players")
            elif inp_choice.casefold() in menu.values():
                # check who won
                if (inp_choice == "p" and comp_choice == "r")\
                        or (inp_choice == "r" and comp_choice == "s")\
                        or (inp_choice == "s" and comp_choice == "p"):
                    print(comp_choice)
                    print("Player wins")
                else:
                    print(comp_choice)
                    print("Computer wins")
            else:
                print("Invalid choice made , please select r, p or s")
        else: print("Quitting game")


if __name__ == "__main__":
    play()