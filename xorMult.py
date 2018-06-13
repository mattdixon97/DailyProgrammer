'''
Preform exculsive or multipication on two integers

https://www.reddit.com/r/dailyprogrammer/comments/6ba9id/20170515_challenge_315_easy_xor_multiplication/
'''

def xorMult(a, b):
    result, i = 0, 1
    while i <= b:
        result = result ^ (a * i * (b & i) // i)
        i *= 2
    return result
