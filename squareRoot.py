'''
Calculates the square root of a number to precision p using Newton's Method

https://www.reddit.com/r/dailyprogrammer/comments/6nstip/20170717_challenge_324_easy_manual_square_root/
'''

# n is the number, p is the precision.
def mysqrt(n, p):
    if (n == 0):
        return 0
    elif (n < 0):
        raise Exception('NaN')
    else:
        return recurSqrt(n, n, p)

def recurSqrt(n,m,p):
    if p == 0:
        return n
    return recurSqrt(nextGuess(n, m), m, p - 1)

def nextGuess(n, m):
    return n - (((n * n) - m) / (2 * n))
