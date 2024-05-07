from grid import Grid,LETTERS
from ship import Ship
mygrid = Grid()

def display_grid():
    
    header= "  A   B   C   D   E   F   G   H   I   J  "
    line  = "+---+---+---+---+---+---+---+---+---+---+"
    edges = ""
    
    print("\n")
    print(header)
    for i in range(1,11):
        for letter in LETTERS:
            cellname = str(i) + letter
            cellvalue = mygrid.grid[cellname]
            edges += f"| {cellvalue} "
        edges += f"| {i}"
        print(line)
        print(edges)
        edges = ""
    print(line)
    print("\n")

"""
display_grid()
# Create a ship and show on grid
ship1 = Ship(["1A","1B","1C"])
ship2 = Ship(["3E","4E","5E"])
mygrid.spawn_ship(ship1)
mygrid.spawn_ship(ship2)
display_grid()
"""

# Game Loop

while True:
    print("Welcome to Battleships!\n")
    command = input("Enter s to start or q to quit:\n")
    if command == "q":
        print("Thanks for playing!")
        break
    print("A quick tutorial:")
    display_grid()