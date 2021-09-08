def board(a):
    print("",a[1]," │",a[2]," │ ",a[3]," ")
    print("────┼────┼────")
    print("",a[4]," │",a[5]," │ ",a[6]," ")
    print("────┼────┼────")
    print("",a[7]," │",a[8]," │ ",a[9]," ")
    

def info():
    print("-----------Welcome To TIC TAC TOE Game By Kiran Narwade------------\n")
    
    players[0] = input("Player 1 Name: ")
    players[1] = input("Player 2 Name: ")
    
    print(players[0],"you are using X")
    print(players[1],"you are using O")
    print("press Enter to start the game")
    enter = input()    
    return enter


# for start game
def startgame():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nthis is ur turn",players[0])
            p = int(input("Please Enter postion : "))
            v = 'x'
            pos[p] = v
            board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 1
                continue
            else:
                print("\nBoomBaam!!,",players[0],"you win this game")
                break
        else:
            print("\nthis is ur turn",players[1])
            p = int(input("Please Enter postion : "))
            v = 'o'
            pos[p] = v
            board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 0
                continue
            else:
                print("\nBoomBaam!!,",players[1],"you win this game")    
                break
    else:
        print("\nGame is Tie")

# winner check function.
def checkwin(v):
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner


# Main Code
pos = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = ['','']
winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
enter = info()

startgame()