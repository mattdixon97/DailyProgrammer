'''
Determine the path travelled by a knight on an infinite chess board to reach a specified co-ordinate

https://www.reddit.com/r/dailyprogrammer/comments/6coqwk/20170522_challenge_316_easy_knights_metric/
'''

from queue import *

moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

"""Adds 2-tuples of ints together"""
def addPairs(a,b):
    x = a[0] + b[0]
    y = a[1] + b[1]
    return x, y

"""Finds the path taken by a knight from (0,0) to goal using BFS"""
def findPath(goal):
    Q = Queue()
    current = {'position': (0,0), 'depth': 0, 'parent': None}
    while True:
        if current['position'] != goal:
            for move in moves:
                newPos = addPairs(current['position'], move)
                newDep = current['depth'] + 1
                nextState = {'position': newPos, 'depth': newDep, 'parent': current}
                Q.put(nextState)
        else:
            return current
        current = Q.get()

"""Prints the path"""
def printPath(finalNode):
    node = finalNode
    path = []
    print("Path: ")
    while node['parent'] != None:
        path.append(node['position'])
        node = node['parent']
    print("(0, 0)")
    for i in range(len(path)-1, -1, -1):
        print(path[i])

def main():
    coords = input("Please enter coordinates: ")
    x, y = coords.split(' ')
    goal = int(x), int(y)
    goalNode = findPath(goal)
    print("Moves needed: ", goalNode['depth'])
    printPath(goalNode)
