'''
Puzzle 29
Define a function that takes an arbitrary number of arguments.
When called, the function should return the number of arguments it was called with.
'''
from typing import Any

def param_count(*args: Any):
    count_args = len(args)
    return count_args
print(param_count())   
