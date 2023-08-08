# Algorithm to solve sudoku code 
N = 9  # declaring variable which will hold number of rows and columns 


def isSafe(sudoku,row,col,num): # here we will create a function that will check if it is okay to assign a number to given row and column , (sud ,r ,c num) as arguments
    for i in range(9): #checking if same number exists in same row by using for loop 
        if sudoku[row][i] == num:
            return False # if present then it will return false


    for i in range(9):
        if sudoku[i][col]== num : #checking if same number exists in same column by using for loop
            return False #if present then it will return false

    startRow = row -row%3 # logic to check number in each box
    startCol = col -col%3
    for i in range(3):   
        for j in range(3):  #here we will check if same number is present in box or not , if present then return false
            if sudoku[startRow + i][startCol + j] == num:
                return False 
    return True #at last it will return true if none of the conditions are satisfied 

def solveSudoku(sudoku,row,col): # this function will assign values to all non assigned locations , it takes sudoku , (starting row num and col num) as arg
    if row == N-1 and col ==N: # checking
        return True #if it is then return true , this conditon will act as base condition since we are using recursion 

    if col == N: # now here we will move to next row when last column is reached 
        row+=1  # increment if condition is satisfied 
        col = 0

    if sudoku[row][col]>0: # here we willnow check if a number is assigned to current position if number at given row and column is > 0 
        return solveSudoku(sudoku,row,col+1) #here will return function to next column 

    for num in range(1,N+1): # using for loop for each num in range so that we can check for each number from 1 to 9 
        if isSafe(sudoku,row,col,num): # now we will check if it is ok to assign this number at given row and column using the previous function we wrote 
            sudoku[row][col]=num # if it is ok to assign the number we will assign it in the sudoku 
                                    # lets assume number assigned is correct
            if solveSudoku(sudoku,row,col+1): # we will also chech for possibility with next column 
                return True

        sudoku[row][col] = 0 # now in the for loops code block we will assign 0 at given position since our assumption was wrong and check the next value 
    return False # returning false at the end of functions code block 

def solver(sudoku): #writing a solved function to sudoku if it  is solvable ,(sud) as arg
    if solveSudoku(sudoku,0,0): # using if cond to check if sud is solvable starting from zeroth row and column 
        return sudoku
    else:
        return "no"


            
