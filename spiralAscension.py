'''
Using inputted number, makes a spiral that begins with 1 and starts from the top left,
spiraling clockwise, and ends with the square of that number.

https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/
'''

def spiral(num):
    sq = num**2
    grid = [[0]*num for _ in range(num)]
    spirals = 0
    currentNum = 0
    while currentNum <= sq:
        for i in range(spirals, (num-spirals)):
            currentNum += 1
            grid[spirals][i] = currentNum
        if currentNum >= sq:
            break
        for j in range(spirals+1, (num-spirals)):
            currentNum += 1
            grid[j][num-spirals-1] = currentNum
        if currentNum >= sq:
            break
        for k in range((num-spirals-2), (spirals-1), -1):
            currentNum += 1
            grid[num-spirals-1][k] = currentNum
        if currentNum >= sq:
            break
        for m in range((num-spirals-2), (spirals), -1):
            currentNum += 1
            grid[m][spirals] = currentNum
        spirals += 1
    return grid

def printGrid(grid):
    num = len(grid)
    maxDigs = len(str(num**2))
    for row in grid:
        for num in row:
            numStr = str(num)
            formNum = numStr.rjust(maxDigs)
            print(formNum, "", end="")
        print()

def main():
    num = int(input("number: "))
    grid = spiral(num)
    printGrid(grid)
