def balanced(s):
    return True if len(s) == 0 else (len(s) / 2) == s.count(s[0])

def balanced_bonus(s):
    return len(set(map(s.count, s))) < 2

