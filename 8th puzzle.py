def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1)
    ]

    for move, dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank]
            )

            neighbors.append((move, tuple(new_state)))

    return neighbors


def depth_limited_dfs(state, goal, depth, path, visited):
    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for move, next_state in get_neighbors(state):
        if next_state not in visited:
            result = depth_limited_dfs(
                next_state,
                goal,
                depth - 1,
                path + [move],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None


def iddfs(start, goal):
    depth = 0

    while True:
        visited = set()

        result = depth_limited_dfs(
            start,
            goal,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

        depth += 1


def read_state(label):
    print(f"Enter the {label} state:")

    values = []

    for _ in range(3):
        values.extend(map(int, input().split()))

    if len(values) != 9:
        raise ValueError("Enter exactly 9 numbers.")

    if sorted(values) != list(range(9)):
        raise ValueError(
            "State must contain numbers 0 to 8 exactly once."
        )

    return tuple(values)


def print_state(state):
    for i in range(0, 9, 3):
        print(*state[i:i + 3])
    print()


def main():
    start = read_state("initial")
    goal = read_state("goal")

    path = iddfs(start, goal)

    if path is None:
        print("No solution found.")
    else:
        print("\nSolution found!")
        print("Moves:", len(path))
        print(" -> ".join(path))


if __name__ == "__main__":
    main()
