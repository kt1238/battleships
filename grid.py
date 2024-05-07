import string
LETTERS = string.ascii_uppercase[0:10]

# 1A is a cell on grid
# Implemented as a dictionary
class Grid:
    
    # Creating grid with cells of value " " and keys of form "1A"
    grid = {}
    for i in range(1,11):
        for letter in LETTERS:
            cellname = str(i) + letter
            grid[cellname] = " "
            
    def set_cell(self, cellname, mark):
        """Update cell with value

        Args:
            cellname (str): key of our cell
            value (str): mark to go in cell X,O
        """
        if self.grid[cellname] == " ":
            self.grid[cellname] = mark
        else:
            print("That cell is occupied")

    def spawn_ship(self, ship):
        for cellname in ship.position:
            self.set_cell(cellname,"P")
        
        
            
    

