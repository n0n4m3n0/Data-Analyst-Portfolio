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
    input_set = set(input_str) #here we make a unique set of letters using the input string
    for i in input_set: 
        if i not in python_list: #then we iterate through the set and check if a letter not in the "python_list"
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
        for j in range(1,i+1): #here we iterate through each number from 1 to i
            if i % j == 0: #in order to check if the number can be divided without a reminder 
                counter += 1 #if it can, then we increase the counter
        if counter == 2: #if the counter is equal to 2(means that there are only two divisors 1 and itself) 
            output.append(i) #we add the number to the output list
        counter = 0 #we reset the counter for the next value in the list
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
    for i in input_str.lower(): #here we iterate through the letters of the input_str
        if i in alphabeth_list: #if the letter is in the alphabeth_list 
            index = alphabeth_list.index(i) #we get the index of this letter from the alphabeth_list 
            index += 13  #we increase the index by 13
            if index > 25: #if the index become larger than 25, then we check the reminder of the divison by modulus
                index = (index % 25) - 1 #and assign it to the index
            output_str = output_str + alphabeth_list[index] #we add to the output string the letter with the new index
        else:
            output_str = output_str + i #else(if the letter is not in the alphabeth_list, we just add the letter as is to the output           
    return output_str 
print(rot13("Cool puzzles!"))    

'''
Puzzle 33
Perform a matrix multiplication, using the following steps:
- Determine the size of the resulting matrix: the resulting matrix will have the same number of rows as the first matrix and the same number of
columns as the second matrix
- Create a matrix of the corrected size with all elements set to zero.
- For each element in the resulting matrix, multiply the elements of the corresponding row in the first matrix and the corresponding column in 
the second matrix
- Sum up the products obtained in the previous step and assign the result to the corresponding element in the resulting matrix
- Repeat steps 3 to 4 for each element of the resulting matrix
- Return the resulting matrix
'''

A = [[2,3],[4,5]]
B = [[10,15],[5,1]]
def matrix_multiply(left_matrix, right_matrix):
    output_matrix = []
    number_of_rows_left = len(left_matrix)
    number_of_columnns_left = len(left_matrix[0])
    number_of_rows_right = len(right_matrix)
    number_of_columns_right = len(right_matrix[0])
    if number_of_columnns_left == number_of_rows_right:    
        for i in range(number_of_rows_left):
          output_matrix.append([0] * number_of_columns_right)
        
        for i in range(number_of_rows_left):
            for j in range(number_of_columns_right):
                for k in range(number_of_rows_right):
                    output_matrix[i][j] += left_matrix[i][k] * right_matrix[k][j]
                  
    else:
        return None                
    print(output_matrix)
matrix_multiply(A, B)  

'''
Puzzle 34
The greatest common divisor of two or more integers is the largest positive integer that divies each of the integers without a reminder.
For example GCD of 8 and 12 is 4.
Define a function that takes two integers. When called, the function should return the greatest common divisor of two integers.
'''

def gcd(num_one:int, num_two:int):
    divisors = []
    output = []
    if num_one > num_two: #here we check witch of the input values is larger, if num_one that proceed with the loop  
        for i in range(1, (num_two + 1)): #for a range of each integer up to num_two 
            if num_two % i == 0: #if num_two divides by this i without reminder 
                divisors.append(i) #we append this i to the divisors list
        for i in divisors: #then for each of the divisor in divisors list
            if num_one % i == 0: #if num_one is divided by the divisor without reminder
                output.append(i) #we append the divisor to the output list  
    else:
        for i in range(1, (num_one + 1)):
            if num_one % i == 0:
                divisors.append(i)
        for i in divisors:
            if num_two % i == 0:
                output.append(i)
    print(output[-1]) #here we took the largest divisors of all
gcd(5,26)           

'''
Puzzle 35
Define a function that takes two parameters.
When called, the function should return a list of all pairs in input_nums whose sum is equal to the target.
The resulting list should not contain duplicate pairs.
'''
from itertools import combinations

def find_pairs_summing_to_target(input_nums, target):
    output = []
    for i in range(1,len(input_nums) + 1):
        combinations_list = list(combinations(input_nums, 2)) # here we create a combination list of pairs from the list
        for combo in combinations_list:
            if sum(combo) == target:
                output.append(combo)
    print(list(set(output))) # set function makes the pairs unique           
find_pairs_summing_to_target([1,7,54,43,2,5,9,2,8], 10)  

'''
Puzzle 36
Insertion sort. Is a simple sorting algorithm that builds the final sorted list one item at a time. It iterates through the input list, and for 
each element in the input list, it compares it to elements that come before it and then insert it in the correct position.
Define a function that takes one parameter: list of integers. The function should implement the insertion sort algorithm and return a sorted list.
'''
def insertion_sort(input_nums):
    for i in range(1, len(input_nums)): # here we take a range from 1 to the lenght of the list
        for j in range(0,i): # here we make an iteration from 0 to the item in the list
            if input_nums[i] < input_nums[j]: # if the current value is less than the previous value, we pop it from the list 
                x = input_nums.pop(i)
                input_nums.insert(j, x) # we insert the poped value in the list in place of the larger value, which we compared  
    print(input_nums)        
insertion_sort([23,34,5,66,12])

'''
Puzzle 37
Define a function int_to_roman that takes one parameter: integer. 
When called, the function should return the input number converted to a roman numeral. You can use only Roman numerals, no other characters are allowed.
'''
roman_map = {
    1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
    90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV",
    1: "I"
    }

def int_to_roman(input_num):
    output = ''
    while input_num > 0:
        max_value = max([i for i in roman_map if i <= input_num]) # here we find a max value among roman integers, which is less or equal to the input integer
        output += roman_map.get(max_value) # we get Roman numeral by the value and append it to the output string       
        input_num = input_num - max_value # we substract the value from the input integer
    print(output)           
int_to_roman(4)        

'''
Puzzle 38
Define a reverse function, which converts a Roman numeral to integer.
'''
def roman_to_integer(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    reversed = roman[::-1] # we reverse the Roman numeral to simplify calculation
    for i in reversed: # then we iterate through each element of the reversed string
        value = roman_dict[i] # we find corresponding values in the roman_dict
        if value < prev_value: # if the value is less than the previous 
            total -= value # we substract it from the total sum  
        else:
            total += value # else we add it to the total sum 
        prev_value = value # rewrite the previous value with the current one
        
    print(total)    
roman_to_integer("MMMMCMXCIX") 
