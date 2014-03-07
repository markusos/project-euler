#!/usr/bin/python

# Returns an array of size 'size' initialized as a spiral
# with value 1 in the center and size^2 in the upper right corner
def spiral(size):
    array = [[0 for i in range(size)] for j in range(size)]

    number = 1
    current = (size // 2, size // 2) 
    direction = (0, 1)
    
    step = 0
    stepsToDirectionChange = 1;
    turns = 0
    
    while number <= size * size:
        # Set current possition to number
        array[current[0]][current[1]] = number
        number += 1
        # Move current to next step
        current = (current[0] + direction[0], current[1] + direction[1])
        step += 1
        # Check if time to turn
        if step == stepsToDirectionChange:
            step = 0
            # Determine the new direction
            if direction[1] == 1:
                direction = (1, 0)
            elif direction[0] == 1:
                direction = (0, -1)
            elif direction[1] == -1:
                direction = (-1, 0)
            else:
                direction = (0, 1)
            # Increase the number of step to next turn
            # after every second turn
            turns += 1
            if turns % 2 == 0:
                stepsToDirectionChange += 1
           
    return  array

# returns the sum of the two diagonals,
# excluding overlaping center possition
def diagonalSum(array):
    size = len(array)

    sum = 0
    for i in range(size):
        sum += array[i][i]
        sum += array[size - i - 1][i]
    return sum - 1
