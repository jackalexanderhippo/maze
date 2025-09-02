import json
import os
from collections import deque
import time


def load_maze(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Maze file {file_path} not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}")
        return None


def is_valid_move(maze, pos, walls_set, visited, width, height):
    row, col = pos
    return (1 <= row <= height and
            1 <= col <= width and
            pos not in walls_set and
            pos not in visited)


def bfs(maze):
    width, height = maze['width'], maze['height']
    start = tuple(maze['start'])
    end = tuple(maze['end'])
    walls_set = {tuple(wall) for wall in maze['walls']}

    if start in walls_set or end in walls_set:
        print(f"Start or end position is a wall in maze")
        return None

    queue = deque([(start, [start])])
    visited = {start}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        (row, col), path = queue.popleft()

        if (row, col) == end:
            return path

        for dr, dc in directions:
            next_pos = (row + dr, col + dc)
            if is_valid_move(maze, next_pos, walls_set, visited, width, height):
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))

    return None  # No path found


def path_to_rc_notation(path):
    return [f"(r{row}c{col})" for row, col in path]


def generate_solution(maze_file, team_name="TeaMu", maze_dir="mazes", solution_dir="solutions"):
    maze = load_maze(os.path.join(maze_dir, maze_file))
    if not maze:
        return None

    start_time = time.time()
    path = bfs(maze)
    execution_time = time.time() - start_time

    if path is None:
        print(f"No valid path found for {maze_file}")
        return None

    solution = {
        "team": team_name,
        "mazeName": maze_file,
        "path": path_to_rc_notation(path),
        "executionTime": f"{execution_time:.2f}"
    }

    os.makedirs(solution_dir, exist_ok=True)

    output_file = os.path.join(solution_dir, f"solution_{maze_file}")
    with open(output_file, 'w') as f:
        json.dump(solution, f, indent=2)

    return solution


def main():
    maze_files = [
        "maze1.json", "maze2.json", "maze3.json", "maze4.json",
        "maze5.json", "maze6.json", "maze7.json", "maze8.json",
        "maze9.json", "maze10.json", "challenge_maze_100.json",
        "challenge_maze_200.json", "anti_bot_maze_200.json"
    ]

    for maze_file in maze_files:
        solution = generate_solution(maze_file)
        if solution:
            print(f"Solution for {maze_file} saved to solutions/solution_{maze_file}")
            print(f"Moves: {len(solution['path']) - 1}, Execution Time: {solution['executionTime']}s")
        else:
            print(f"Failed to generate solution for {maze_file}")


if __name__ == "__main__":
    main()