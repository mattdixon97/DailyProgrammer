'''
Translate a phrase to leetspeak

https://www.reddit.com/r/dailyprogrammer/comments/67dxts/20170424_challenge_312_easy_l33tspeak_translator/
'''

def toLeet(char):
    return {'A': '4',     'B': '6',     'E': '3',
            'I': '1',     'M': '(V)',   'L': '1',
            'N': '(\)',   'O': '0',     'S': '5',
            'T': '7',     'V': '\/',    'W': '`//'
            }[char]

def translate():
    keepGoing = True
    while keepGoing:
        output = ''
        string = input("Input the phrase you want translated to l33t: ")
        string = string.upper()
        for char in string:
            try:
                output += toLeet(char)
            except KeyError:
                output += char
        print(output)
        end = input("Press ENTER to translate again or enter 'Q' to quit \n")
        if end.upper() == "Q":
            keepGoing = False
