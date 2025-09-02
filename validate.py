import os
import json


def get_maze_solve_path(maze_json):
    # path is e.g. ["(r1c1)", "(r1c2)", "(r2c2)"]
    return None, None


if __name__ == "__main__":
    for maze_fname in os.walkdir('mazes'):
        maze_json = json.load(maze_fname)
        solution_path, execution_time = get_maze_solve_path()
        solution_json = {
            "team": "TeMu",
            "mazeName": maze_fname,
            "path": solution_path,
            "executionTime": execution_time
        }

        print(solution_json)