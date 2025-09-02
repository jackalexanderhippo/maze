# Maze Runner Challenge - Maze Files

This directory contains all the maze files you'll need for the Maze Runner Hackathon. These files represent mazes of varying complexity and size that your algorithm will need to solve.

## Maze File Structure

Each maze is provided as a JSON file with the following structure:

```json
{
  "width": 100,      // Width of the maze
  "height": 100,     // Height of the maze
  "start": [2, 99],  // Starting position [row, column]
  "end": [99, 2],    // Ending position [row, column]
  "walls": [         // Array of wall positions [row, column]
    [1, 1], 
    [1, 2],
    // ... more wall coordinates
  ]
}
```

**Important Notes:**
- All coordinates are 1-indexed (positions start at 1, not 0)
- Coordinates are in [row, column] format
- The maze is bounded by the specified width and height
- You can only move up, down, left, or right (no diagonal moves)
- You cannot move through walls

## Maze Types and Difficulty Levels

The maze files are organized into three levels of difficulty:

### Level 1: Standard Mazes
- `maze1.json` to `maze5.json`: Small hedge mazes (10x10 to 30x30)
- Perfect for testing your initial algorithm implementation
- Reasonable memory requirements

### Level 2: Medium Difficulty
- `maze6.json` to `maze10.json`: Medium-sized mazes (30x30 to 50x50)
- More complex pathways
- Tests basic optimization of your algorithm

### Level 3: Challenge Mazes
- `challenge_maze.json`, `challenge_maze_100.json`, `challenge_maze_200.json`: Advanced mazes with strategic traps (100x100 to 200x200)
- `anti_bot_maze_200.json`: Specifically designed to challenge common pathfinding heuristics
- Tests advanced pathfinding capabilities and memory efficiency

## Solution Template

The `solution_template.json` file provides the format for your solution submissions:

```json
{
  "team": "YOUR_TEAM_NAME",
  "mazeName": "MAZE_FILE_NAME",
  "path": [
    "(r1c1)",
    "(r1c2)",
    "..."
  ],
  "executionTime": 0.00
}
```

Your path should be an ordered array of coordinates from start to end, where each coordinate is in the format `(rXcY)` where:
- `r` represents the row number
- `c` represents the column number
- Both are 1-indexed

For example, the coordinate `(r3c4)` represents the position at row 3, column 4.

## Visualization

It's highly recommended to visualize the mazes to better understand their structure. 

## Validation

Remember to validate your solutions before submission. A valid solution must:
- Start at the specified start point
- End at the specified end point
- Only move between adjacent cells (no diagonal moves)
- Never go through walls
- Have a continuous path with no breaks

Good luck, and may the best algorithm win!
