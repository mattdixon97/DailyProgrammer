'''
Takes a 24-hour time and translates it into words

https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
'''

def readTime():
    time = input().split(':')
    h, m = int(time[0]), int(time[1])
    isAM, h = divmod(h, 12)
    hour, minute = str(h), str(m)
    out = "It's "
    out += getHour(hour) + " "
    if m < 20:
        if m < 10:
            out += "o'"
            if m == 0:
                out += "clock"
        out += getMinOnes(minute) + " "
    else:
        out +=  getMinTens(minute[0])
        if int(minute[1]) != 0:
            out += "-"
        out += getMinOnes(minute[1]) + " "
    out += ["am", "pm"][isAM]
    return out

def getHour(hour):
    return{ "0": "twelve",  "1": "one",      "2": "two",      "3": "three",  "4": "four",
            "5": "five",    "6": "six",      "7": "seven",    "8": "eight",  "9": "nine",
            "10": "ten",    "11": "eleven",  "12": "twelve"
    }[hour]

def getMinTens(minTens):
    return{ "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty"}[minTens]

def getMinOnes(minOnes):
    return{ "0": "",          "1": "one",         "2": "two",        "3": "three",
            "4": "four",      "5": "five",        "6": "six",        "7": "seven",
            "8": "eight",     "9": "nine",        "10": "ten",       "11": "eleven",
            "12": "twelve",   "13": "thirteen",   "14": "fourteen",  "15": "fifteen",
            "16": "sixteen",  "17": "seventeen",  "18": "eighteen",  "19": "nineteen"
    }[minOnes]

def main():
    time = readTime()
    print(time)
