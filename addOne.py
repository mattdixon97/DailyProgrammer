'''
Create a new number by adding one to each digit of a number 

https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/
'''

def addOne(n):
        return int(''.join([str(int(x) + 1) for x in str(n)]))

