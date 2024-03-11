#!/usr/bin/python3
import sys


def canUnlockAll(boxes):
    sys.setrecursionlimit(1000000)  # SET RECURSION LIMIT NUMBER.
    un_boxes = [False] * len(boxes)

    def unlock(boxes, index):
        try:
            # change the value to true if false (box not open), but if
            # the value is true (box has already been unlocked), exit.
            if not un_boxes[index]:
                un_boxes[index] = True
            else:
                return

            keys = boxes[index]
            if not keys:
                return

            for i in keys:
                unlock(boxes, i)

        except IndexError:
            return

    unlock(boxes, 0)
    return all(un_boxes)
