
turncount=0

grid=[0,[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
def board():
    print(grid[1][3],grid[2][3],grid[3][3])
    print(grid[1][2],grid[2][2],grid[3][2])
    print(grid[1][1],grid[2][1],grid[3][1])
def turnp1():
    global turncount
    if turncount==9:
        board()
        print("TIE")
    else:
        board()
        print("P1 Turn. (X)")
        x=turnx()
        y=turny()
        if grid[x][y]=="X" or grid[x][y]=="O":
            print("Sorry, can't do")
            turnp1()
        else:
            grid[x][y]="X"
            turncount+=1
            if grid[1][1]==grid[1][2]==grid[1][3]=="X" or grid[1][1]==grid[2][2]==grid[3][3]=="X" or grid[2][1]==grid[2][2]==grid[2][3]=="X" or grid[3][1]==grid[3][2]==grid[3][3]=="X" or grid[1][1]==grid[2][1]==grid[3][1]=="X" or grid[1][2]==grid[2][2]==grid[3][2]=="X" or grid[1][3]==grid[2][3]==grid[3][3]=="X" or grid[1][3]==grid[2][2]==grid[3][1]=="X":
                board()
                print("Epic win for P1")
            else:
                turnp2()

def turnp2():
    global turncount
    if turncount==9:
        board()
        print("TIE")
    else:
        board()
        print("P2 Turn. (O)")
        x=turnx()
        y=turny()
        if grid[x][y]=="X" or grid[x][y]=="O":
            print("Sorry, can't do")
            turnp2()
        else:
            grid[x][y]="O"
            turncount+=1
            if grid[1][1]==grid[1][2]==grid[1][3]=="O" or grid[1][1]==grid[2][2]==grid[3][3]=="O" or grid[2][1]==grid[2][2]==grid[2][3]=="O" or grid[3][1]==grid[3][2]==grid[3][3]=="O" or grid[1][1]==grid[2][1]==grid[3][1]=="O" or grid[1][2]==grid[2][2]==grid[3][2]=="O" or grid[1][3]==grid[2][3]==grid[3][3]=="O" or grid[1][3]==grid[2][2]==grid[3][1]=="O":
                board()
                print("Epic win for P2")
            else:
                turnp1()

def turnx():
    turn1x=int(input("Input x axis of the turn, must be between 1 and 3 (including 1 and 3)"))
    if turn1x<1 or turn1x>3:
        print("Sorry, can't do")
        return turnx()
    else:
        return turn1x
def turny():
    turn1y=int(input("Input y axis of the turn, must be between 1 and 3 (including 1 and 3)"))
    if turn1y<1 or turn1y>3:
        print("Sorry, can't do")
        return turny()

    else:
        return turn1y

def option():
    global turncount
    AI=int(input("Press 1 to play 2 player, press 2 to play single player"))
    if AI==1:
        turnp1()
    elif AI==2:
        aiturn(turncount)
    else:
        print("bruh")
        option()

def aiturnp1():
    if grid[1][1]==grid[1][2]==grid[1][3]=="X" or grid[1][1]==grid[2][2]==grid[3][3]=="X" or grid[2][1]==grid[2][2]==grid[2][3]=="X" or grid[3][1]==grid[3][2]==grid[3][3]=="X" or grid[1][1]==grid[2][1]==grid[3][1]=="X" or grid[1][2]==grid[2][2]==grid[3][2]=="X" or grid[1][3]==grid[2][3]==grid[3][3]=="X" or grid[1][3]==grid[2][2]==grid[3][1]=="X":
        board()
        print("Epic win for humanity")
    elif grid[1][1]==grid[1][2]==grid[1][3]=="O" or grid[1][1]==grid[2][2]==grid[3][3]=="O" or grid[2][1]==grid[2][2]==grid[2][3]=="O" or grid[3][1]==grid[3][2]==grid[3][3]=="O" or grid[1][1]==grid[2][1]==grid[3][1]=="O" or grid[1][2]==grid[2][2]==grid[3][2]=="O" or grid[1][3]==grid[2][3]==grid[3][3]=="O" or grid[1][3]==grid[2][2]==grid[3][1]=="O":
        board()
        print("The singularity is coming")
    else:
        global turncount
        if turncount==10:
            board()
            print("TIE")
        else:
            board()
            print("P1 Turn. (X)")
            x=turnx()
            y=turny()
            if grid[x][y]=="X" or grid[x][y]=="O":
                print("Sorry, can't do")
                aiturnp1()
            else:
                grid[x][y]="X"
                turncount+=1
                if grid[1][1]==grid[1][2]==grid[1][3]=="X" or grid[1][1]==grid[2][2]==grid[3][3]=="X" or grid[2][1]==grid[2][2]==grid[2][3]=="X" or grid[3][1]==grid[3][2]==grid[3][3]=="X" or grid[1][1]==grid[2][1]==grid[3][1]=="X" or grid[1][2]==grid[2][2]==grid[3][2]=="X" or grid[1][3]==grid[2][3]==grid[3][3]=="X" or grid[1][3]==grid[2][2]==grid[3][1]=="X":
                    board()
                    print("Epic win for P1")
                else:
                    aiturn(turncount-1)

def aiturn(turn):
    global turncount
    if turncount==10:
        board()
        print("TIE")
    elif turn==0:
        grid[1][1]="O"
        turncount+=1
        aiturnp1()
    elif turn==1:
        if grid[2][3]=="X" or grid[3][2]=="X":
            grid[2][2]="O"
            turncount+=1
            aiturnp1()
        elif grid[1][3]=="X" or grid[3][1]=="X":
            grid[3][3]="O"
            turncount+=1
            aiturnp1()
        elif grid[1][2]=="X":
            grid[3][1]="O"
            turncount+=1
            aiturnp1()
        elif grid[2][1]=="X" or grid[3][3]=="X":
            grid[1][3]="O"
            turncount+=1
            aiturnp1()
        elif grid[2][2]=="X":
            grid[3][3]="O"
            turncount+=1
            aiturnp1()

    elif turn==3:
        if grid[2][2]=="O" and grid[2][3]=="X":
            if grid[3][3]=="X":
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[3][3]="O"
                turncount+=1
                aiturnp1()
        elif grid[2][2]=="O" and grid[3][2]=="X":
            if grid[3][3]=="X":
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[3][3]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][3]=="O" and grid[1][3]=="X":
            if grid[2][2]=="X":
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][2]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][3]=="O" and grid[3][1]=="X":
            if grid[2][2]=="X":
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][2]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][1]=="O" and grid[1][2]=="X":
            if grid[2][1]=="X":
                grid[3][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][1]="O"
                turncount+=1
                aiturnp1()
        elif grid[1][3]=="O" and grid[2][1]=="X":
            if grid[1][2]=="X":
                grid[3][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[1][2]="O"
                turncount+=1
                aiturnp1()
        elif grid[1][3]=="O" and grid[3][3]=="X":
            if grid[1][2]=="X":
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[1][2]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][3]=="O" and grid[2][2]=="X":
            if grid[2][3]=="X":
                grid[2][1]="O"
                turncount+=1
                aiturnp1()
            elif grid[1][3]=="X":
                grid[3][1]=="O"
                turncount+=1
                aiturnp1()
            elif grid[1][2]=="X":
                grid[3][2]="O"
                turncount+=1
                aiturnp1()
            elif grid[3][2]=="X":
                grid[1][2]="O"
                turncount+=1
                aiturnp1()
            elif grid[3][1]=="X":
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
            elif grid[2][1]=="X":
                grid[2][3]="O"
                turncount+=1
                aiturnp1()
    elif turn==5:
        if grid[1][3]=="O" and grid[2][2]=="O":
            if grid[3][1]=="X":
                grid[1][2]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][1]=="O" and grid[2][2]=="O":
            if grid[1][3]=="X":
                grid[2][1]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][3]=="O" and grid[3][1]=="O":
            if grid[2][1]=="X":
                grid[3][2]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][1]="O"
                turncount+=1
                aiturnp1()
        elif grid[1][3]=="O" and grid[3][3]=="O":
            if grid[2][3]=="X":
                grid[1][2]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][3]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][1]=="O" and grid[3][3]=="O":
            if grid[2][2]=="X":
                grid[3][2]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][2]="O"
                turncount+=1
                aiturnp1()
        elif grid[1][3]=="O" and grid[3][3]=="O":
            if grid[2][2]=="X":
                grid[2][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][2]="O"
                turncount+=1
                aiturnp1()
        elif grid[1][3]=="O" and grid[3][1]=="O":
            if grid[2][2]=="X":
                grid[2][1]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][2]="O"
                turncount+=1
                aiturnp1()
        else:
            if grid[3][1]=="X":
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
            elif grid[2][1]=="X":
                grid[2][3]="O"
                turncount+=1
                aiturnp1()
            elif grid[3][2]=="X":
                grid[1][2]="O"
                turncount+=1
                aiturnp1()
            elif grid[1][2]=="X":
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
            elif grid[1][3]=="X":
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
            elif grid[2][3]=="X":
                grid[2][1]="O"
                turncount+=1
                aiturnp1()
    elif turn==7:
        if grid[2][3]=="X":
            if grid[3][1]=="X":
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
        elif grid[1][3]=="X":
            if grid[2][1]=="X":
                grid[3][2]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[2][1]="O"
                turncount+=1
                aiturnp1()
        elif grid[1][2]=="X":
            if grid[3][1]=="X":
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
        elif grid[2][1]=="X":
            if grid[1][3]=="X":
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][1]=="X":
            if grid[1][2]=="X":
                grid[2][3]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[1][2]="O"
                turncount+=1
                aiturnp1()
        elif grid[3][2]=="X":
            if grid[1][3]=="X":
                grid[3][1]="O"
                turncount+=1
                aiturnp1()
            else:
                grid[1][3]="O"
                turncount+=1
                aiturnp1()
    elif turn==9:
        if grid[1][1]==" ":
            grid[1][1]="O"
            turncount+=1
            aiturnp1()
        elif grid[1][2]==" ":
            grid[1][2]="O"
            turncount+=1
            aiturnp1()
        elif grid[1][3]==" ":
            grid[1][3]="O"
            turncount+=1
            aiturnp1()
        elif grid[2][1]==" ":
            grid[2][1]="O"
            turncount+=1
            aiturnp1()
        elif grid[2][2]==" ":
            grid[2][2]="O"
            turncount+=1
            aiturnp1()
        elif grid[2][3]==" ":
            turncount+=1
            aiturnp1()
        elif grid[3][1]==" ":
            turncount+=1
            aiturnp1()
        elif grid[3][2]==" ":
            grid[3][2]="O"
            turncount+=1
            aiturnp1()
        elif grid[3][3]==" ":
            grid[3][3]="O"
            turncount+=1
            aiturnp1()
            
            
        

    




option()

