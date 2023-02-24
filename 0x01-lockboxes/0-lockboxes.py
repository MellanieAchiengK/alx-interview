#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes): #pylint: disable=invalid-name
    """
    Checks if all boxes can be opened or not.

    Arguments:
    boxes -- list of lists with keys for each box

    Returns: True if all boxes can be opened, False otherwise
    """
    # Number of boxes
    n = len(boxes) #pylint: disable=invalid-name

    if n <= 0:
        return False

    # Keeps track of opened boxes
    opened_boxes = [False]*n

    # Open first box
    opened_boxes[0] = True

    # Iterates through boxes
    for i in range(n):
        # If current box is unlocked
        if opened_boxes[i]:
            # Iterates through keys in current box
            for key in boxes[i]:
                if 0 <= key < n and not opened_boxes[key]:
                    # Unlocks the new box
                    opened_boxes[key] = True

    # Checks if all boxes have been opened
    if False in opened_boxes:
        return False

    return True
