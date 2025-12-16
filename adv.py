def has_roll(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
        return 0
    return grid[row][col] == '@'
    
def count_adj(grid, row, col, max_rolls):
    rolls = 0
    spots = [[row-1, col-1], [row-1, col], [row-1, col+1],
            [row, col-1],                   [row, col+1],
            [row+1, col-1], [row+1, col], [row+1, col+1]]
    for spot in spots:
        rolls+= has_roll(grid, spot[0], spot[1])
    return rolls < max_rolls        

allowed = 0
grid = []
with open("code.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if grid[row][col] == '@':
            allowed += count_adj(grid, row, col, 4)
        

print(f"Allowed {allowed}")
