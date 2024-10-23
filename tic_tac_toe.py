# Code by SHIVKALP.
def create_grid(size):
    #column = []
    grid = []
    for i in range(size):
        rows = []
        for j in range(size):
            rows.append(" ")
        grid.append(rows)
        
    return grid
    
def display_grid1(size, grid):    
    print("-------")
    for i in range(size):
        for j in range(size):
            print("|"+grid[i][j], end="")
        print("|")
        print("-------")  
        
def check_if_match(size, grid):
    a_mark = []
    b_mark = []
    for i in range(size):
        a_mark.append('O')
        b_mark.append('X')
    for i in range(size):    
        row_elements = grid[i]
        column_elements = [column[i] for column in grid]
        if (row_elements == a_mark) or (column_elements == a_mark):
            print("Player - A won the match.")
            exit()
        elif (row_elements == b_mark) or (column_elements == b_mark):
            print("Player - B won the match.")
            exit()
        
def initialize(size):
    grid = create_grid(size)
    display_grid1(size, grid)
    row,col = 0,0
    
    #Now, player_a will start the game initially. We will ask both the players to give the input in terms of row and column.
    for i in range(size*size):
        #Consider, for every even value of i, player_a will mark. And, for every odd value of i, player_b will mark.
        if (i%2==0):
            row = int(input("Enter row first"))
            col = int(input("Enter column now"))
            grid[row][col] = 'O'
            display_grid1(size, grid)
            check_if_match(size, grid)
            
        elif (i%2==1):
            row = int(input("Enter row first"))
            col = int(input("Enter column now"))
            grid[row][col] = 'X'
            display_grid1(size, grid)
            check_if_match(size, grid)
            
    print("Ohh, it's a tie!!!!, better luck next time....")
                          
               
#grid = display_grid1(3)
#print(grid)
#Players - player_a and player_b. player_a will mark with 'O' and player_b will mark with 'X'.
size = int(input("Enter the size of grid"))
initialize(size)