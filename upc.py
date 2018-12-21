'''
Given an 11-digit number, find the check digit that would make a vaild UPC.
https://en.wikipedia.org/wiki/Universal_Product_Code#Check_digit_calculation

https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/
'''

# python3 wont allow an int with leading 0, so
# upc takes a str param
def upc(n):
    return (10 - (sum(map(int, n[::2])) * 3 + sum(map(int, n[1::2]))) % 10) % 10
