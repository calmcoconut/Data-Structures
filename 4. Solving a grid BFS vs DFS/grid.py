"""
File: grid.py
"""

from arrays import Array

class Grid(object):
    """Represents a two-dimensional array."""

    def __init__(self, rows, columns, fillValue = None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)

    def getHeight(self):
        """Returns the number of rows."""
        return len(self._data)

    def getWidth(self):
        "Returns the number of columns."""
        return len(self._data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [][]."""
        return self._data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result

# def main():

def maze_reader(input):
    #bring in data from file
    with open(input) as f:
        grid_data = f.readlines()
    columns = len(grid_data[0])-1 #-1 due to \n
    #setup grid object with no values
    rows = len(grid_data)
    g = Grid(rows, columns, '*')
    # print(g)
    # use raw data to replace *'s with actual values
    for i in grid_data:
        x = 0
        grid_data[x] = grid_data[x].rstrip()
        x +=1
    column_bits = []
    row = 0
    column = 0
    while row < rows:
        #make string into list
        current_iteration = list(grid_data[row])
        for byte in current_iteration:
            if byte != '\n':
                g[row][column] = byte
                # print("assigned row, ",row, "column to, ",column, "  ",byte)
                column += 1
            else:
                pass
            # else:
            #     row += 1
            #     column = 0
        column = 0
        row += 1
    # print(g)
    return g

grid = maze_reader('maze1.txt')
f = open("test.txt","w")

# with f as file:
#     f.write(str(grid))

print(grid,  file=open('test.txt', 'w'))




# if __name__ == "__main__": main()
    

