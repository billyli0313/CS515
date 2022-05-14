'''
Created on 4/29/2022
@author:   JIanfei Li
Pledge:    I pledge that I have done the homework by myself
CS515 - Hw 13 - Board class
'''
class Board(object):
    
    def __init__(self, width=7, height=6):
        '''Initializes width, height and the board'''
        self.width = width 
        self.height = height 
        board = []
        for _ in range(1,self.height + 1):
            board += [[' '] * self.width] 
        self.data = board
        
    def __str__(self):
        '''Returns a nice string representation of the board'''
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '-' * (self.width * 2 + 1) + '\n'
        s += ' 0 1 2 3 4 5 6 '
        return s
    
    def allowsMove(self, col):
        '''Checks to see if user is allowed to make move in the game'''
        if col >= self.width or col < 0:
            return False 
        elif self.data[0][col] != ' ': 
            return False
        else:
            return True 
    
    def addMove(self, col, ox):
        '''Make user's move and add it to the board if possible'''
        i = self.height - 1
        while i > -1:
            if self.data[i][col] == ' ':
                self.data[i][col] = ox
                i = -1
            else:
                i -= 1 
    
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.
            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            
    def delMove(self, col):
        '''Removes the top checker from col'''
        i = 0
        while i < self.height:
            if self.data[i][col] != ' ':
                self.data[i][col] = ' '
                i = self.height
            else:
                i += 1 
                
    def horizontalCheck(self, ox):
        '''Horizontal Win Checker'''
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and self.data[row][col + 1] == ox and self.data[row][col + 2] == ox and self.data[row][col + 3] == ox:
                    return True 
                    
    def verticalCheck(self, ox):
        '''Vertical Win Checker'''
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.data[row][col] == ox and self.data[row + 1][col] == ox and self.data[row + 2][col] == ox and self.data[row + 3][col] == ox:
                    return True 
        
    def diagonalCheck1(self, ox):   
        '''First Diagonal Win Checker''' 
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and self.data[row + 1][col + 1] == ox and self.data[row + 2][col + 2] == ox and self.data[row + 3][col + 3] == ox:
                    return True
        
    def diagonalCheck2(self,ox):
        '''Second Diagonal Win Checker'''
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.data[row][col] == ox and self.data[row + 1][col - 1] == ox and self.data[row + 2][col - 2] == ox and self.data[row + 3][col - 3] == ox:
                    return True
                
    def winsFor(self, ox):
        '''Checks board to see if the user won by getting 4 in a row'''            
        if self.horizontalCheck(ox) == True or self.verticalCheck(ox) == True or self.diagonalCheck1(ox) == True or self.diagonalCheck2(ox) == True:
            return True 
        else:
            return False 
                
    def hostGame(self):
        '''Runs loop allowing users to play Connect 4
           player = 1 is X; player = 2 is O'''
        print('Welcome to Connect Four!' + '\n')
        player = 1
        while True:
            print(self) 
            if player == 1:
                print('\n')
                choice = input("X's choice: ")
                if self.allowsMove(int(choice)) == True:
                    self.addMove(int(choice),'X')
                    print('\n')
                    if self.winsFor('X') == True:
                        print('X wins -- Congratulations!' + '\n')
                        print(self) 
                        break
                    else:
                        print(self)
                        player = 2
                else:
                    player = 1
                    
            if player == 2: 
                print('\n')
                choice = input("O's choice: ")
                if self.allowsMove(int(choice)) == True:
                    self.addMove(int(choice),'O')
                    print('\n')
                    if self.winsFor('O') == True:
                        print('O wins -- Congratulations!' + '\n')
                        print(self)
                        break
                    else:
                        player = 1
                else:
                    player = 2
                    
           
    
if __name__ == '__main__':
    b = Board(7, 6)
    b.hostGame()

    

