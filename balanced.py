'''
Determines if there is the same number of two chars in a string
Bonus: Determines if every letter in a string appears the same number of times

https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/
'''

def balanced(s):
    return True if len(s) == 0 else (len(s) / 2) == s.count(s[0])

def balanced_bonus(s):
    return len(set(map(s.count, s))) < 2

