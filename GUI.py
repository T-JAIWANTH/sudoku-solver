from tkinter import *
from solver import solver # importing solver from solver file (module)

root = Tk()
root.title("Suduko Solver") # title
root.geometry("324x550")  #dimension

label = Label(root,text = "Fill in the numbers and click solve").grid(row = 0,column = 1,columnspan = 10)

errLabel = Label(root,text=" ",fg="red")
errLabel.grid(row = 15 ,column = 1,columnspan = 10 ,pady=5) # it will be displayed during error

solvedLabel = Label(root,text="",fg="green")
solvedLabel.grid(row = 15 ,column = 1,columnspan = 10 ,pady=5) # displayed if suduko is solved correctly

cells = {} # here we will store each cell in input

def ValidateNumber(P): # this function will control what is enterd into cells , it will take value of cell as argument
    out = (P.isdigit() or P == "")and len(P)<2 # it checks the value if it is digit or empty string which allow user to delete value ,to restrict the value to one digit "and" is used "len" 
    return out # returning the value of boolean expression 

reg = root.register(ValidateNumber)  #registering the function to the window using root register method

def draw3x3Grid(row ,column ,bgcolor): #dividing "9x9" to "3x3" by def function in which row ,col,bg as argument
    for i in range(3): #indicates rows
        for j in range(3): #indicates columns
            e = Entry(root,width = 5 , bg = bgcolor , justify = "center"  , validate = "key" , validatecommand=(reg,"%P")) #creating entery widget , justify to center align the text , validating to key to call validate function upon key press , validate command to registered function , %p will pass the new value to function upon change
            e.grid(row=row+i+1 , column=column+j+1 , sticky = "nsew",padx = 1,pady = 1 , ipady = 5 ) # placing the widget at sum of row number(i+1 row) and sum of column number(j+1) , setting sticky to nsew which will make it sticky from all directions ,(internal padding y ) 
            cells[(row+i+1 , column+j+1)] = e #storing the entery widget into the dictionary with tuple of row and column that we used to place the widget as a key


def draw9x9Grid(): # function for drawing "9x9" grid 
    color = "#D0ffff"# two color combo 
    for rowNo in range(1,10,3): #for loop with step size 3 
        for colNo in range(0,9,3):# for loop with step size 3 
            draw3x3Grid(rowNo , colNo , color) # calling "3x3" grid and passing row no col no to it
            if color == "#D0ffff": #using if condition to alternate b/w colors , if value of color variable is first color we will set it to second color
                color = "#ffffd0"
            else:
                color = "#D0ffff" #else it will be set to first color

def clearValues(): #this function will clear the values in each cell of the grid 
    errLabel.configure(text ="") # clearing the error and success labels 
    solvedLabel.configure(text="") 
    for row in range(2,11): #again iterating through rows and columns
        for col in range(1,10): # ranges are different here
            cell = cells[(row,col)] # here we are getting the entry widget stored in the dictionary at given row and column 
            cell.delete(0,"end") # using the delete method of the entery widget to delete its value from index zero to the end 

def getValues(): #wrting get values function 
    board = [] # declaring an empty list where we will store the  values for each cell for each row 
    errLabel.configure(text="") #again clearing the labels to clear any text in them if any 
    solvedLabel.configure(text = "") 
    for row in range(2,11): # loop  for iterating through rows
        rows = [] #creating empty list for each row
        for col in range(1,10): # loop for iterating through columns 
            val = cells[(row,col)].get() #getting the values of the cell using entry widgets method 
            if val == "":  
                rows.append(0) # if value is an empty string we will append a zero to rows list 
            else:
                rows.append(int(val)) # else we will append int(values) to the list 


        board.append(rows) # now after inner for loop append the rows list to the boards list 
    updateValues(board)  # (afetr importing) calling upd values  func and passing board matrix to it 
    
        
btn = Button(root,command = getValues , text = "Solve",width = 10) #creating button , command will be set to get values function 
btn.grid(row=20,column = 1 ,columnspan=5 , pady = 20)


btn = Button(root,command = clearValues , text = "Clear",width = 10)  # command set for clear values 
btn.grid(row=20,column = 5 ,columnspan=5 , pady = 20)

def updateValues(s): # (afetr importing) this function will update values in the cells and display solutions of sudoku ,(sudoku matrix as argument)
    sol = solver(s) #calling solver function and passing sudoku to it
    if sol!= "no": #condition
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end") #deleting existing values from cell
                cells[(rows,col)].insert(0,sol[rows-2][col - 1]) #using insert method to insert values at zeroth index (the value will be num at row - 2nd row and column - 1st column) ( we are subt 2 and 1 respectively since matrix is zero indexed)
        solvedLabel.configure(text="Sudoku solved!") # after the for loop set text method of solved label to sudoku solved using configure method 
    else:  
        errLabel.configure(text="No solution exists for this sudoku") #in eelse part text will be set to no soln exists 

draw9x9Grid() #calling
root.mainloop() #launching















        










            
