#!/usr/bin/env python3
""" Rotate 2D matrix """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise. """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)
