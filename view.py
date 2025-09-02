import json
import matplotlib.pyplot as plt

def visualize_maze(json_file):
    # Load maze data
    with open(json_file, "r") as f:
        maze = json.load(f)

    width, height = maze["width"], maze["height"]
    start = tuple(maze["start"])
    end = tuple(maze["end"])
    walls = set(map(tuple, maze["walls"]))

    # Initialize grid
    grid = [[0 for _ in range(width)] for _ in range(height)]

    # Mark walls
    for (x, y) in walls:
        if 1 <= x <= width and 1 <= y <= height:
            grid[height - y][x - 1] = 1  # invert y so it matches coordinates

    # Plot maze
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="binary")

    # Mark start and end
    plt.scatter(start[0] - 1, height - start[1], c="green", s=120, marker="o", label="Start")
    plt.scatter(end[0] - 1, height - end[1], c="red", s=120, marker="X", label="End")

    plt.title(f"Maze Visualization ({width}x{height})")
    plt.xticks(range(width))
    plt.yticks(range(height))
    plt.grid(visible=True, color="gray", linewidth=0.5)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Example: save your JSON into "maze.json"
    visualize_maze("mazes/maze1.json")
