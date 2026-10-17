#Initializing vars
state = ""
list1 = []
list2 = []
counter = 1

with open("level1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    list1.append(int(lines[0][0]))
    print(list1)
    for line in lines:
        if len(list2) > list1[0]:
            list2.append(lines[5+counter])
            counter+=1
    print(list2)

#def get_mushroom:

    

    


while True:
    match state:
        case "np":
            intro_screen()
        case "played":
            playing_screen()
        case "gg":
            gameOver()
        