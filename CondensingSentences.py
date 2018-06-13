'''
Condensing a sentence by removing overlapping letters from the end of one word and the start of the next.

https://www.reddit.com/r/dailyprogrammer/comments/6grwny/20170612_challenge_319_easy_condensing_sentences/
'''

def match(word, nextWord):
    r = 0
    for i in range(1, min(len(word), len(nextWord))):
        if word[-i:] == nextWord[:i]:
            r = i
    return r

def condense(sentence):
    words = sentence.split()
    outStr = ""
    for i in range(len(words)-1):
        r = match(words[i], words[i+1])
        if r > 0:
            words[i+1] = words[i] + words[i+1][r:]
            words[i] = ""
        else:
            outStr += words[i] + " "
    print(outStr + words[-1])
