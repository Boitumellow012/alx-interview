#!/usr/bin/python3
"""
    Define the Pascal Triangle function
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        triangle = pascal[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        pascal.append(temp)

    return pascal
