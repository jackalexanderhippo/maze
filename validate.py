import os
import json


def get_maze_solve_path(maze_json):
    # path is e.g. ["(r1c1)", "(r1c2)", "(r2c2)"]
    return None, None


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

    # Convert path from R1C1 notation to coordinates
    try:
        coords = []
        for pos in path:
            if not (pos.startswith('R') and 'C' in pos):
                return 5000
            r, c = pos.split('C')
            r = r[1:]  # Remove 'R'
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


def validate_solution(solution_file, maze_dir=""):
    solution = load_solution(solution_file)
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
    solution_files = [f"mazes/solution_maze{i}.json" for i in range(1, 11)]

    for solution_file in solution_files:
        if os.path.exists(solution_file):
            moves = validate_solution(solution_file)
            print(f"Validation for {solution_file}: {moves} moves")
        else:
            print(f"Solution file {solution_file} not found")


if __name__ == "__main__":
    main()
    # for maze_fname in os.walkdir('mazes'):
    #     maze_json = json.load(maze_fname)
    #     solution_path, execution_time = get_maze_solve_path()
    #     solution_json = {
    #         "team": "TeMu",
    #         "mazeName": maze_fname,
    #         "path": solution_path,
    #         "executionTime": execution_time
    #     }
    #
    #     print(solution_json)

