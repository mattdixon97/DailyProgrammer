'''
Computes a slightly modified version of the Collatz sequence

https://www.reddit.com/r/dailyprogrammer/comments/6e08v6/20170529_challenge_317_easy_collatz_tag_system/
'''

def collatzTag(string):
    alphabet = {'a':'bc','b':'a','c':'aaa'}
    while len(string) > 1:
        string = string[2:] + alphabet[string[0]]
        print(string)
