# Created by Alejandro at 
# 10/21/2019
"""
# Solves a maze given a grid and it's starting point using a stack approach.
Ending point must be a "T"

# Can you conclude anything from the differences in these results?
Stack finished the maze with 202 choices whereas queue finished the maze with 259 choices.
this speaks to the different nature of the two data structures.
Stacks have a Last in First Out approach and as such will continue down a path before trying a different path
Queues, on the other hand, have a first in first out approach and will visit each possible neighboring option before
moving on.
# Are there best cases and worst cases of the maze problems for stacks and queues?
To follow-up on the reasoning above:
Stacks will perform as depth first and will have a worse case when there are many paths to the goal. This is because
this approach may not give the shortest path.

Queues will perform as breadth first and will perform worse case the more path options there are as they will attempt
to visit all neighboring cells before moving on and will have to keep these multiple possible paths in memory.
"""
from grid import maze_reader
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue


starting_point = 4,0 #row, column
_current = starting_point


def mazeSolver(maze, start,to_text=False,data_structure='stack'):
    """takes a maze and its starting point (as a tuple of row, column) and solves the maze. Maze walls must be *
    characters and the ending point must be a "T" character. Free spaces must be an empty space, " ". """
    # read the grid and set up stack
    grid = maze_reader(maze)
    print("maze without attempts:\n", grid)
    if data_structure == 'stack':
        _queue = LinkedStack()
    else:
        _queue = LinkedQueue() #TODO implement a linkedQueue structure with push
    _queue.push(start)
    # track choices:
    choice_count = 0
    #use stack data structure to explore maze and find a path to the end.
    while not _queue.isEmpty():
        _pop = _queue.pop()
        # print("popping ",_pop)
        if grid[_pop[0]][_pop[1]] == 'T':
            choice_count += 1
            print("Finished maze: \n")
            print(grid)
            if to_text:
                maze_text(grid,"solution.txt")
            return choice_count
        else:
            # if the _pop location did not return the character "T", leave a breadcrumb to not revisit.
            if grid[_pop[0]][_pop[1]] != 'O' and grid[_pop[0]][_pop[1]] != 'T' and grid[_pop[0]][_pop[1]] != 'P':
                choice_count += 1
                grid[_pop[0]][_pop[1]] = 'O'
            # print("grid row, column is ",_pop[0],_pop[1],"\n")
            # print(grid)
            left = grid[_pop[0]][(_pop[1]-1)]
            right =  grid[_pop[0]][(_pop[1]+1)]
            down = grid[(_pop[0]-1)][_pop[1]]
            up = grid[(_pop[0]+1)][_pop[1]]
            if left == ' ' or left == 'T':
                _queue.push((_pop[0],(_pop[1]-1)))
            if right == ' ' or right == 'T':
                _queue.push((_pop[0],(_pop[1]+1)))
            if up == ' ' or up == 'T':
                _queue.push(((_pop[0]+1),_pop[1]))
            if down == ' ' or down == 'T':
                _queue.push(((_pop[0]-1),_pop[1]))
    #if stack becomes empty, there is no path.
    return choice_count

def maze_text(grid,file_name):
    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col])
            result += "\n"
        return result
    grid.__str__ = __str__
    f = open(file_name,"w")
    with f as file:
        f.write(str(grid))

def main():
    x = mazeSolver('maze1.txt', starting_point, to_text=True)
    print(x)
    y = mazeSolver('maze1.txt', starting_point, to_text=True,data_structure='queue')
    print(y)
if __name__ == "__main__":
    main()