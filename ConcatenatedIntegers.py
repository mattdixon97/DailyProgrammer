'''
Determine largest and smallest values that can be created by concatenation

https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/
'''

import itertools

def concatInts():
    string = input("Numbers: ")
    array = []
    lst = list(itertools.permutations(string.split(" ")))
    for i in range(len(lst)):
        array.append(int("".join(x for x in lst[i])))
    array.sort()
    print(array[0], array[-1])
