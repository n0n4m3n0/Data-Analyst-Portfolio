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

'''
Puzzle 30
Define a function, that takes one parameter: a string.
When called, the function should return a boolean value indicating whether the string contains any combination of the word "python".
The letters of "python" can be in any order. e.g. "nohtyp" but must not be interrupted by any other characters. The function should be case-insensitive.
'''
python_list = ["P", "Y", "T", "H", "O", "N"]

def contains_python_chars(input_str: str):
    input_str = input_str.upper()
    input_set = set(input_str)
    print(input_set)
    for i in input_set:
        print(i)
        if i not in python_list:
            return False
    return True    
        
print(contains_python_chars("pyThon"))

'''
Puzzle 31
Define a function that takes a list of integers from input. When called, the function should return a new list containing only the prime numbers.
The prime number is a positive integer, which is divided by 1 and itself.
'''
def find_primes(input_nums):
    counter = 0
    output = []
    for i in input_nums:
        for j in range(1,i+1):
            if i % j == 0:
                counter += 1
        if counter == 2:
            output.append(i)
        counter = 0
    return output    
print(find_primes([1,2,3,4,5,11,13,17]))      

'''
Puzzle 32
ROT13 is a simple encryption mechanism, which replaces each letter in a message with the letter 13 positions ahead of it in the alphabet. For example, "A"
becomes "N". If there are no letter to shift forward, you should wrap around and start from the beginning.
Define a function rot13 that takes one parameter: a string.
When called, the function should return a new string which has been encrypted using ROT13. Numbers and symbols should not be rotated.
'''
alphabeth_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
                  "v","w","x","y","z"]

def rot13(input_str: str):
    output_str = ""
    for i in input_str.lower():
        if i in alphabeth_list:
            index = alphabeth_list.index(i)
            index += 13 
            if index > 25:
                index = (index % 25) - 1
            output_str = output_str + alphabeth_list[index]
        else:
            output_str = output_str + i            
    return output_str 
print(rot13("Cool puzzles!"))    
