def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print (board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    
     
def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or #across the top
    (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or #across the middle
    (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or #across the bottom
    (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or #down left side
    (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or #down the middle
    (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or #down the right side
    (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or #diagoal
    (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player)) #diagonal

      
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #Choosing who goes
    for i in range(9): #Available spaces
        printBoard(board) #Generating the board
        print('Turn for ' + turn + '. Move on which space?') #Asking the player what space they want to choose
        move = input() #Choose move
        board[move] = turn #Move happens
        if( checkWinner(board, 'X') ): #Checking if move wins
            print('X wins!') #If move wins for x then the win is printed
            break #End game if won
        elif ( checkWinner(board, 'O') ):#Check to see if 0 wins
            print('O wins!') #If o wins then print win sign
            break #End game if won and if not then game continues
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
