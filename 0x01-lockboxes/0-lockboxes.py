#!/usr/bin/python3
'''Solution to ALX intereview question 2'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened.'''
    unlocked = []

    def dfs(box):
        keys = boxes[box]

        if box not in unlocked:
            unlocked.append(box)

            for box in keys:
                dfs(box)

    dfs(0)
    if len(unlocked) != len(boxes):
        return False
    return True
