
def is_variable(t):
    return isinstance(t, str) and t[0].islower()

def is_compound(t):
    return isinstance(t, tuple)

def to_str(t):
    if is_compound(t):
        return f"{t[0]}({', '.join(to_str(a) for a in t[1:])})"
    return t

def apply_subst(t, theta):
    if is_variable(t) and t in theta:
        return apply_subst(theta[t], theta)
    if is_compound(t):
        return (t[0],) + tuple(apply_subst(a, theta) for a in t[1:])
    return t

def occurs_check(var, t, theta):
    if var == t:
        return True
    if is_variable(t) and t in theta:
        return occurs_check(var, theta[t], theta)
    if is_compound(t):
        return any(occurs_check(var, a, theta) for a in t[1:])
    return False

def unify(x, y, theta):
    if theta is None:
        return None
    if x == y:
        return theta
    if is_variable(x):
        return unify_var(x, y, theta)
    if is_variable(y):
        return unify_var(y, x, theta)
    if is_compound(x) and is_compound(y):
        if x[0] != y[0] or len(x) != len(y):
            return None
        for a, b in zip(x[1:], y[1:]):
            theta = unify(a, b, theta)
            if theta is None:
                return None
        return theta
    return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    if is_variable(x) and x in theta:
        return unify(var, theta[x], theta)
    if occurs_check(var, x, theta):
        return None
    new_theta = dict(theta)
    new_theta[var] = x
    return new_theta

tests = [
    (('Knows', 'John', 'x'), ('Knows', 'John', 'Jane')),
    (('Knows', 'John', 'x'), ('Knows', 'y', 'Mary')),
    (('Knows', 'John', 'x'), ('Knows', 'x', 'Elizabeth')),
]

if __name__ == "__main__":
    for i, (e1, e2) in enumerate(tests, start=1):
        print(f"Test {i}")
        print("Expression 1 :", to_str(e1))
        print("Expression 2 :", to_str(e2))
        theta = unify(e1, e2, {})
        if theta is None:
            print("Result       : Unification FAILED (not unifiable)")
        else:
            subs = ", ".join(f"{v}/{to_str(apply_subst(t, theta))}" for v, t in theta.items())
            print("Unifier      : {" + subs + "}")
        print()