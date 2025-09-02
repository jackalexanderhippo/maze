import json
import os


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


def load_solution(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Solution file {file_path} not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}")
        return None


def validate_path(maze, path):
    if not path:
        return 5000

    # Convert path from (rxcy) notation to coordinates
    try:
        coords = []
        for pos in path:
            if not (pos.startswith('(r') and pos.endswith(')') and 'c' in pos):
                return 5000
            # Remove parentheses and split by 'c'
            pos = pos[1:-1]  # Remove ( and )
            r, c = pos.split('c')
            r = r[1:]  # Remove 'r'
            coords.append((int(r), int(c)))
    except (ValueError, IndexError):
        return 5000

    walls_set = {tuple(wall) for wall in maze['walls']}
    width, height = maze['width'], maze['height']
    start, end = tuple(maze['start']), tuple(maze['end'])

    # Check start and end
    if coords[0] != start or coords[-1] != end:
        return 5000

    # Check each position is within bounds and not a wall
    for row, col in coords:
        if not (1 <= row <= height and 1 <= col <= width) or (row, col) in walls_set:
            return 5000

    # Check moves are adjacent and valid
    for i in range(len(coords) - 1):
        r1, c1 = coords[i]
        r2, c2 = coords[i + 1]
        if abs(r1 - r2) + abs(c1 - c2) != 1:  # Not adjacent (not horizontal or vertical move)
            return 5000

    return len(path) - 1  # Number of moves (excluding start position)


def validate_solution(solution_file, maze_dir="mazes", solution_dir="solutions"):
    solution = load_solution(os.path.join(solution_dir, solution_file))
    if not solution:
        return 5000

    maze_name = solution.get('mazeName')
    if not maze_name:
        print(f"Error: No mazeName in {solution_file}")
        return 5000

    maze_file = os.path.join(maze_dir, maze_name)
    maze = load_maze(maze_file)
    if not maze:
        return 5000

    moves = validate_path(maze, solution['path'])
    return moves


def main():
    solution_files = [
                         f"solution_maze{i}.json" for i in range(1, 11)
                     ] + [
                         "solution_challenge_maze_100.json",
                         "solution_challenge_maze_200.json",
                         "solution_anti_bot_maze_200.json"
                     ]

    for solution_file in solution_files:
        moves = validate_solution(solution_file)
        print(f"Validation for {solution_file}: {moves} moves")


if __name__ == "__main__":
    main()