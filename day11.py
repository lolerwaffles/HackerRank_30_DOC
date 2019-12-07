inputLine = input()
grid = []
sumIs = []
while inputLine != None:
    grid.append(inputLine.split())
    try:
        inputLine = input()
    except:
        inputLine = None

for i in range(len(grid)):
    for j in range(len(grid[0])):
        I = 0
        try:
            I += int(grid[i][j])+int(grid[i][j+1])+int(grid[i][j+2])
            I += int(grid[i+1][j+1])
            I += int(grid[i+2][j])+int(grid[i+2][j+1])+int(grid[i+2][j+2])
            sumIs.append(I)
        except:
            pass
print(sorted(sumIs)[-1])
