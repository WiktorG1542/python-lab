def is_balanced(exp: str):
    l = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for a in exp:
        if a in bracket_pairs.values():
            l.append(a)
        elif a in bracket_pairs.keys():
            if not l or l[-1] != bracket_pairs[a]:
                return False
            l.pop()

    return len(l) == 0

print(is_balanced("([]{[]})"))
print(is_balanced("([]{[]}"))
print(is_balanced("([)]"))
print(is_balanced("{[()]}"))
