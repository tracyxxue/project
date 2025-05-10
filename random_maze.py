import random

def generate_maze(rows, cols):
    maze = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if i == 0:
                # First row: random 0 or 1
                row.append(random.randint(0, 1))
                # If there's a 1 above, favor generating a 1
            else:
                if j < len(maze[i-1]) and maze[i - 1][j] == 1:
                    row.append(1 if random.random() < 0.7 else 0)
                else:
                    row.append(random.randint(0, 1))
        maze.append(row)
     #replace a 1 with a 1 directly above in the last row to 2
        if i == rows - 1 and 2 not in row:
            for j, item in enumerate(row):
                if item ==1 and maze[i-1][j]==1:
                    maze[i][j]=2
                    break
            
        
    # Ensure every row has at least one 1
    #if not, generate a 1 with a 1 above
    for i, row in enumerate(maze):
        if 1 not in row and 2 not in row:
            if i == 0:                        
                maze[0][0] = 1  
            else:
                for j in range(cols):
                    if maze[i - 1][j] == 1:
                        maze[i][j] = 1
                        break
    #Ensure in every row there is a 1 that has 
    # a 1 directly above
    for i, row in enumerate(maze):
        check=0
        for j, col in enumerate(row):
            if (col==1 or col==2) and maze[i-1][j]==1:
                check+=1
        if check<1:
            for j in range(cols):
                if maze[i - 1][j] == 1:
                    maze[i][j] = 1
                    break

    return maze