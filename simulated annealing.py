import math
import random


def simulated_annealing(cost, initial_state, neighbor,
                        T_start=100.0, T_end=1e-3, alpha=0.95,
                        iters_per_temp=100):
    """
    cost          : function(state) -> float (lower is better)
    initial_state : starting solution
    neighbor      : function(state) -> a new state close to the given one
    T_start       : initial temperature
    T_end         : stop when temperature falls below this
    alpha         : cooling rate (T = alpha * T)
    iters_per_temp: moves tried at each temperature
    """
    current = initial_state
    current_cost = cost(current)
    best, best_cost = current, current_cost
    T = T_start

    while T > T_end:
        for _ in range(iters_per_temp):
            candidate = neighbor(current)
            candidate_cost = cost(candidate)
            delta = candidate_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / T):
                current, current_cost = candidate, candidate_cost

                if current_cost < best_cost:
                    best, best_cost = current, current_cost

        T *= alpha  

    return best, best_cost

def f(x):
    return x ** 2 + 10 * math.sin(x)


def random_neighbor(x):
    return x + random.uniform(-1, 1)


if __name__ == "__main__":
    start = random.uniform(-10, 10)
    best_x, best_f = simulated_annealing(f, start, random_neighbor)
    print(f"Best x = {best_x:.4f}")
    print(f"Best f(x) = {best_f:.4f}")