#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    openBoxes = []
    counter = 0
    total_boxes = len(boxes)
    for key in boxes[0]:
        if key < total_boxes and key not in openBoxes:
            openBoxes.append(key)
            counter += 1

    index = 0
    while index < len(openBoxes):
        for key in boxes[openBoxes[index]]:
            if key < total_boxes and key not in openBoxes and key > 0:
                openBoxes.append(key)
                counter += 1

        index += 1
    if counter == len(boxes) - 1:
        return True
    else:
        return False
