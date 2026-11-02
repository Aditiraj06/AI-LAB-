import random

def generate_random_state(N):
    return [random.randint(0, N-1) for i in range(N)]

def calculate_conflicts(state):
    conflicts = 0
    N = len(state)

    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                conflicts += 1

    return conflicts

def generate_neighbors(state):
    neighbors = []
    N = len(state)

    for col in range(N):
        for row in range(N):
            if state[col] != row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)

    return neighbors

def hill_climbing(N):
    if N == 2 or N == 3:
        print("No solution exists")
        return

    for restart in range(1000):
        state = generate_random_state(N)
        conflicts = calculate_conflicts(state)

        while conflicts != 0:
            neighbors = generate_neighbors(state)

            best_state = state
            best_conflicts = conflicts

            for neighbor in neighbors:
                count = calculate_conflicts(neighbor)

                if count < best_conflicts:
                    best_conflicts = count
                    best_state = neighbor

            if best_conflicts >= conflicts:
                break
            else:
                state = best_state
                conflicts = best_conflicts

        if conflicts == 0:
            print("Solution found:", state)
            print("Number of conflicts:", conflicts)

            for row in range(N):
                for col in range(N):
                    if state[col] == row:
                        print("Q", end=" ")
                    else:
                        print(".", end=" ")
                print()

            return

    print("Solution not found after maximum restarts")

N = int(input("Enter number of queens: "))

if N < 1:
    print("Invalid input")
else:
    hill_climbing(N)