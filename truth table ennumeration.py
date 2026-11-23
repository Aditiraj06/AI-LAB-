from itertools import product


def NOT(a):         return not a
def AND(a, b):      return a and b
def OR(a, b):       return a or b
def IMPLIES(a, b):  return (not a) or b
def IFF(a, b):      return a == b
kb_text = "(P -> Q) ^ P"
query_text = "Q"
symbols = ['P', 'Q']

def KB(m):
    return AND(IMPLIES(m['P'], m['Q']), m['P'])

def query(m):
    return m['Q']

def tt_entails(kb, alpha, symbols):
    entails = True
    kb_true_models = 0

    print("Knowledge Base :", kb_text)
    print("Query          :", query_text)
    print("Symbols        :", symbols)
    print()

    for i, values in enumerate(product([True, False], repeat=len(symbols)), start=1):
        model = dict(zip(symbols, values))
        kb_val = kb(model)
        q_val = alpha(model)

        print(f"Model {i}: {model}")
        print(f"   KB = {kb_val}, Query = {q_val}")

        if kb_val:
            kb_true_models += 1
            if not q_val:
                entails = False

    print()
    print(f"Result: KB is true in {kb_true_models} model(s).")
    if entails:
        print(f"Conclusion: KB entails {query_text}, because the query is true in every model where KB is true.")
    else:
        print(f"Conclusion: KB does NOT entail {query_text}, because there is a model where KB is true but the query is false.")

    return entails

if __name__ == "__main__":
    tt_entails(KB, query, symbols)