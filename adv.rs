use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn has_roll(grid: &Vec<Vec<char>>, row: usize, col: usize) -> isize {
    if row >= grid.len() || col >= grid[0].len(){
        return 0;
    }
    return (grid[row][col] == '@') as isize;
}

fn count_adj(grid: &Vec<Vec<char>>, row: isize, col:isize, max:isize) -> i32{
    let mut rolls = 0;
    let spots = vec![(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col -1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)];
    for (row, col) in spots{
        rolls += has_roll(grid, row as usize, col as usize);
    }
    return (rolls < max) as i32;
}

fn main() -> io::Result<()> {
    
    let reader = io::BufReader::new(File::open(Path::new("code.txt"))?);
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in reader.lines() {
        let line = line?;
        let row: Vec<char> = line.chars().collect();
        grid.push(row);
    }
    let mut allowed = 0;
    for row in 0..grid.len(){
        for col in 0..grid[row].len(){
            if grid[row][col] == '@'{
                allowed += count_adj(&grid, row as isize, col as isize, 4);
            }
        }
    }
    println!("Allowed {}", allowed);
    return Ok(());
}
