def is_var(t):
    return isinstance(t, str) and t[0].islower()

def unify(x, y, s):
    if s is None: return None
    if x == y: return s
    if is_var(x): return unify_var(x, y, s)
    if is_var(y): return unify_var(y, x, s)
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            s = unify(a, b, s)
            if s is None: return None
        return s
    return None

def unify_var(v, x, s):
    if v in s: return unify(s[v], x, s)
    if is_var(x) and x in s: return unify(v, s[x], s)
    return {**s, v: x}

def subst(t, s):
    if is_var(t) and t in s: return subst(s[t], s)
    if isinstance(t, tuple): return tuple(subst(a, s) for a in t)
    return t

def match(premises, kb, s):
    if not premises:
        yield s
        return
    for f in kb:
        t = unify(premises[0], f, s)
        if t is not None:
            yield from match(premises[1:], kb, t)

fmt = lambda t: f"{t[0]}({', '.join(t[1:])})"

facts = [('Parent', 'Tom', 'Bob'), ('Parent', 'Bob', 'Ann')]
premises = [('Parent', 'x', 'y'), ('Parent', 'y', 'z')]
conclusion = ('Grandparent', 'x', 'z')
query = ('Grandparent', 'Tom', 'Ann')

print("Facts :", ", ".join(map(fmt, facts)))
print("Rule  : Parent(x, y) ^ Parent(y, z) => Grandparent(x, z)")
print("Query :", fmt(query))

kb = list(facts)
changed = True
while changed:
    changed = False
    for s in list(match(premises, kb, {})):
        new = subst(conclusion, s)
        if new not in kb:
            kb.append(new)
            print("Derived:", fmt(new))
            changed = True

print("Result:", "Query is TRUE" if query in kb else "Query cannot be derived")