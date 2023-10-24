"""
Standard built-in functions of JavaScripts base
"""


# Array.prototype.find()
def find(predicate, iterable, default=None):
    for item in iterable:
        if predicate(item):
            return item
    return default

# Array.prototype.every()
def every(predicate, iterable):
    return all(predicate(item) for item in iterable)

# Array.prototype.some()
def some(predicate, iterable):
    return any(predicate(item) for item in iterable)