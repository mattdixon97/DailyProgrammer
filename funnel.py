'''
Find the longest word funnel for a given word

https://www.reddit.com/r/dailyprogrammer/comments/99d24u/20180822_challenge_366_intermediate_word_funnel_2/
'''

import requests

r = requests.get('https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt')
wordlist = r.content.decode('utf-8').split('\n')

word_funnel = []        # current word funnel being explored
max_funnel = []         # word funnel of the longest length


# returns list of all strings created by removing one letter from str param word
def substrings(word):

	substrs = []

	for i in range(len(word)):
		substrs.append(word[:i] + word[i+1:])

	return substrs


# returns true if target str found in wordlist
def binSearch(wordlist, target):

	lower = 0
	upper = len(wordlist) - 1

	while lower <= upper:

		mid = (lower + upper) // 2

		if wordlist[mid] < target:
			lower = mid + 1
		elif wordlist[mid] > target:
			upper = mid - 1
		else:
			return True

	return False


# finds longest word funnel for given word and saves it to global var max_funnel
def funnel(word):

    global word_funnel, max_funnel

    if len(word_funnel) == 0:
        word_funnel.append(word)

    for w in substrings(word):
        if binSearch(wordlist, w):
            word_funnel.append(w)
            funnel(w)

    if len(word_funnel) > len(max_funnel):
        max_funnel = word_funnel

    word_funnel = word_funnel[:-1]


def main(word):
    funnel(word)
    for i in range(len(max_funnel)-1):
        print(max_funnel[i] + " => ", end='')
    print(max_funnel[-1])
