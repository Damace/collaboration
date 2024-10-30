# utils.py

def reductor(n):
    if n <= 0:  # Base case
        return n
    return reductor(n - 1)  # Recursive call that moves closer to the base case
