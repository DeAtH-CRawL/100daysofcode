print('''

      
     *                                        !
      _.---._       !                         |>>>
    .'       '.     |>>>   *                  |>>>     *
   /           \    |>>>                      |               !
  |             |   |                   *    /~\              |>>>  
  |             |  /~\        _             /~~~\             |>>>   *
   \           /  /~~~\    /\(")/\         /~~~~~\  *  _   _  |_   _   _
    '.       ,'  /~~~~~\  //\   /\\       /~~~~~~~\   | |_| |_| |_| |_| |
      !'---'`   /~~~~~~~\ `  `m`  `      /~~~~~~~~~\ [___________________]
      |>>>     /~~~~~~~~~\              /~~~~~~~~~~~\ |           _     |
      |>>>  !  U_U_U_U_U_U         __  U _ U U U U U U|         .'|'.   |
 *    |     |>>>\ \| |/ /      _  (OO)_.'/ \ | | / / /|         |oo=|   |
     /~\    |>>> |  _  |       \'._)   .'___________/ |         |_|_|   |
    /~~~\   |    |.'|'.|        '..-'._ `'._   _   |  |   _             |
   /~~~~~\ /~\   ||=OO||    *          '.__.'.'|'. |  | .'|'.           |
  /~~~~~~~\~~~\  ||_|_||                 |   |=+=| |  | |=+=|           |
 (XXXXXXXXX)~~~\ |     |         !       |   |_|_| |  | |_|_|           |
  |   _   |xxxxx)U_U_U_U_U_U_U   |>>>    |         |_ |                 |
  | .'|'. |[]  | \ \  | |  / /   |>>>    |     _   | \|    _________    |
  | |=+=| | _  |_ |         | _  |_   _  |_  .'|'. |  |   [_________]   |
  | |_|_| || |_| ||  .-.    || |_| |_| |_| | |OO=| |  __   |XXXXXXX|    |
  |   _   |       |  | |    |    %     %   | |_|_| |_(oo)  _\/\/\/\|    |
  | .'|'. |       |  |_|    |    |'._.'|   |       |   (_.'/ " " " |    |
  | |=+=|_|   __  |         |    |__|  |   |       |_.'-..'|       |    |
  | |_|_|\'._(oo) | _       |    |'. .'|   |.---.  |  |____|_______|____|
  |   _   `.    (_.'/   .-. |    \  '  /   ||   |  | /~~~~/=========\~~~
~"| .'|'_.'  _.'-..'    | | |     '._.'    ||_  |  |/~~~~/...........\~~
  | |=+'.__.'     |     |_| |          _   ||   |  |~^"^/_____________\~^
  | |_|_| |       |         |     _    )\  ||___|__|
  |       |_______|         |_____))_.'~~'.|    ~"^"
  |       |~^^"^~"|_________|~^~.'~~'.x  x :
  lc______|        "~"^"~~"^~  : x  x :~~_.'
  ~"^"~"^"                      `-~~-'"^"^"^^
                           ~^"~^"~^

''')


#python choose your own adventure game
print("welcome to treasure island.\nYour mission is to find the treasure")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "right":
    print("You fell into a hole. Game Over.")
elif choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Invalid choice. Game Over.")