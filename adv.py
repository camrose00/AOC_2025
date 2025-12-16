grid = []
with open("code.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

def has_roll(grid, row, col) -> int:
    try:
        if row < 0 or col < 0:
            return 0
        if row > len(grid):
            return 0
        if col > len(grid[row]):
            return 0
        
        if grid[row][col] == '@':
            # print(f"Has roll: {row}x{col}  {grid[row][col]}")
            return 1
    except Exception as e:
        # print(f"E {e}")
        return 0
    
    return 0
    


def count_adj(grid, row, col, max_rolls):
    rolls = 0
    #count top three
    spots = [[row-1, col-1], [row-1, col], [row-1, col+1],
            [row, col-1],                   [row, col+1],
            [row+1, col-1], [row+1, col], [row+1, col+1]]
    for spot in spots:
        rolls+= has_roll(grid, spot[0], spot[1])
    if rolls < max_rolls:
        print(f"Allowed {spot}")
        return 1
    return 0

allowed = 0


for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if grid[row][col] == '@':
            allowed += count_adj(grid, row, col, 4)
        

print(allowed)

