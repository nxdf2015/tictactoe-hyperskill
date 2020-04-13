


x="X"
o="O"
players=[o,x]
size_board=3
initial_state=["_"*3]*3

def getCell():
    """
    return a list of string ["xxx","__o","xxx"]
    """
    elems=input("Enter cells: ")
    row=[]
    cell=[]
    for elem in elems:
       row.append(elem)
       if len(row)==size_board:
           cell.append("".join(row + []))
           row=[]

    return cell

def columns(cells):
    return [ "".join([ cells[row][col] for row in range(size_board) ]) for col in range(size_board) ]

def diagonals(cells):
    return ["".join([cells[i][i] for i in range(size_board)]),
    "".join([cells[3-i-1][i] for i in range(size_board)])]

def isWin(player,cells):
    rowWin=player*3
    test_row=[  row== rowWin for row  in cells]
    test_col =[col== rowWin for col in columns(cells)]
    test_diag=[diag==rowWin for diag in diagonals(cells)]
    return any(test_col+test_row+test_diag)


def countEmpty(cells):
    """
    return number empty cells
    """
    return "".join(cells).count("_")


def getState(cells):

    x_win = isWin(x,cells)
    o_win =isWin(o,cells)

    if abs("".join(cells).count(x) - "".join(cells).count(o)) > 1 or (x_win and o_win):
        return "Impossible"
    elif x_win:
        return f"{x} wins"
    elif o_win:
        return f"{o} wins"
    elif countEmpty(cells) > 0:
        return "Game not finished"
    else:
        return "Draw"

def board(cells):
   return "\n".join(["-" * 9]+[f"|{row.replace('',' ')}|" for row in cells]+["-" * 9])


def show_board(cells):
    """
    append line '-' top bottom
    print cells
    """
    print(board(cells))


def getCoordinate():
    while True:
        try:
            x,y=list(map(int,input("Enter the coordinates: ").split()))
            if 1<= x <= 3 and 1 <= y <= 3:
                #coordinate valid
                return (x,4-y)
            else:
                print("Coordinate should be from 1 to 3!")
        except:
            print("You should enter numbers!")



def validateCoordinate(x,y,cells):
    return  cells[y-1][x-1] == "_"

def updateRow(x,player,row):
    update=""
    for i in range(size_board):
        if   i == x-1:
            update+=player
        else:
            update+=row[i]
    return update


def updateCell(x,y,player,cells):
    """
    update cells[y-1][x-1] with player
    """
    update=[]
    for i in range(size_board):
        if not  i == y-1:
            update.append(cells[i])
        else:
            update.append(updateRow(x,player,cells[i]))
    return update

def changePlayer(player):
    return o if player == x else x
def play(player,cells):
    """
    ask player coordinate
    validate coordinate
    update board
    return a new board updated
    """
    while True:
        (x,y) = getCoordinate()

        if validateCoordinate(x,y,cells):
            # valid cell
            return updateCell(x,y,player,cells)

        else:
            print("This cell is occupied! Choose another one!")


def loop():
    player=x
    cells=initial_state
    show_board(cells)
    while True:
        cells=play(player,cells)
        state=getState(cells)
        show_board(cells)
        if not state=="Game not finished":
            print(state)
            break
        player=changePlayer(player)



loop()
