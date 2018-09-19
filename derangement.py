'''
Calculate the subfactorial of n, defined as the derangement of a set of n elements.
https://en.wikipedia.org/wiki/Derangement

https://www.reddit.com/r/dailyprogrammer/comments/9cvo0f/20180904_challenge_367_easy_subfactorials_another/
'''

from math import factorial

# standard implementation
def derangement(n):
	if n == 0:
		return 1
	elif n == 1:
		return 0
	else:
		return (n-1) * (derangement(n-1) + derangement(n-2))


# one-liner
def derangement2(n):
	return 1 if n == 0 else 0 if n == 1 else (n-1) * (derangement(n-1) + derangement(n-2))


# non-recursive one-liner
def derangement3(n):
        return int(factorial(n) * sum([(-1)**i / factorial(i) for i in range(n+1)]))
