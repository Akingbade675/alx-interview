#!/usr/bin/python3
'''Solution to ALX intereview question 2'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened.'''
    unlocked = []

    def dfs(box):

        if box < len(boxes):
            unlocked.append(box)

            keys = boxes[box]

            for box in keys:
                if box not in unlocked:
                    dfs(box)

    dfs(0)
    if len(unlocked) != len(boxes):
        return False
    return True
