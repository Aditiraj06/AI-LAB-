import heapq

GOAL = ((1, 2, 3),
        (8, 0, 4),
        (7, 6, 5))

GOAL_POS = {GOAL[r][c]: (r, c) for r in range(3) for c in range(3)}

def h_misplaced(state):
    count = 0
    for r in range(3):
        for c in range(3):
            if state[r][c] != 0 and state[r][c] != GOAL[r][c]:
                count += 1
    return count

def h_manhattan(state):
    total = 0
    for r in range(3):
        for c in range(3):
            tile = state[r][c]
            if tile != 0:
                gr, gc = GOAL_POS[tile]
                total += abs(r - gr) + abs(c - gc)
    return total

def get_neighbors(state):
    neighbors = []

    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                br, bc = r, c

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = br + dr, bc + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            board = [list(row) for row in state]
            board[br][bc], board[nr][nc] = board[nr][nc], board[br][bc]
            neighbors.append(tuple(tuple(row) for row in board))

    return neighbors

def a_star(start, heuristic):
    g = 0
    h = heuristic(start)
    f = g + h

    open_list = [(f, g, start, [start])]
    best_g = {start: 0}
    closed = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == GOAL:
            return path, g

        if state in closed:
            continue

        closed.add(state)

        for nb in get_neighbors(state):
            new_g = g + 1

            if nb in closed:
                continue

            if nb not in best_g or new_g < best_g[nb]:
                best_g[nb] = new_g
                new_h = heuristic(nb)
                new_f = new_g + new_h
                heapq.heappush(open_list, (new_f, new_g, nb, path + [nb]))

    return None, -1

def print_board(state):
    for row in state:
        print(*row)
    print()

start = ((2, 8, 3),
         (1, 6, 4),
         (7, 0, 5))

for name, h in [("Tiles Out of Place", h_misplaced),
                ("Manhattan Distance", h_manhattan)]:

    path, moves = a_star(start, h)

    print("Heuristic:", name)

    if path is None:
        print("No solution\n")
        continue

    for step in path:
        print_board(step)

    print("Number of moves:", moves, "\n")