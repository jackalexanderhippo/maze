import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import re

def parse_path(path_strings):
    """
    Convert path like ["(r1c1)", "(r1c2)", "(r2c2)"]
    into [(col, row), ...] coordinates (1-based to match maze).
    """
    coords = []
    for step in path_strings:
        match = re.match(r"\(r(\d+)c(\d+)\)", step)
        if match:
            row, col = int(match.group(1)), int(match.group(2))
            coords.append((col, row))  # store as (x, y)
    return coords


def visualize_maze_with_path(json_file, path_strings):
    # Load maze data
    with open(json_file, "r") as f:
        maze = json.load(f)

    width, height = maze["width"], maze["height"]
    start = tuple(maze["start"])
    end = tuple(maze["end"])
    walls = set(map(tuple, maze["walls"]))

    # Initialize grid
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for (x, y) in walls:
        if 1 <= x <= width and 1 <= y <= height:
            grid[height - y][x - 1] = 1

    # Convert path into coordinates
    path = parse_path(path_strings)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(grid, cmap="binary")

    # Plot start and end
    ax.scatter(start[0] - 1, height - start[1], c="green", s=120, marker="o", label="Start")
    ax.scatter(end[0] - 1, height - end[1], c="red", s=120, marker="X", label="End")

    # Path marker (blue dot)
    marker, = ax.plot([], [], "bo", markersize=12, label="Path")

    def init():
        marker.set_data([], [])
        return marker,

    def update(frame):
        x, y = path[frame]
        marker.set_data(x - 1, height - y)
        return marker,

    ani = animation.FuncAnimation(
        fig, update, frames=len(path),
        init_func=init, blit=True, interval=500, repeat=False
    )

    ax.set_title("Maze Path Animation")
    ax.set_xticks(range(width))
    ax.set_yticks(range(height))
    ax.grid(visible=True, color="gray", linewidth=0.5)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    # Example path
    path_example = ["(r2c3)", "(r3c3)", "(r4c3)", "(r4c4)", "(r5c4)"]

    visualize_maze_with_path("mazes/maze1.json", path_example)
