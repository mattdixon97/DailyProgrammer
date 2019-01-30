'''
Calculate the additive persistence of a number
http://mathworld.wolfram.com/AdditivePersistence.html

https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/
'''

def persistence(n, p=1):
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s > 9:
        p += persistence(s,p)
    return p

