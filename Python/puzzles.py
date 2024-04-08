'''
Puzzle 1
Filter an input list of words. If there is letter 'a' in the word, it is added to the output list.
'''

user_input = ['apple', 'banana', 'something']
list_a = [] 
for x in user_input:
    for y in x:
        if y == 'a':
            list_a.append(x)
            break
print(list_a) 

'''
Puzzle 2
Define a function sum_if_less_than_fifty that takes two parameters:
When called, the function should return either: The sum of the two numbers if the sum is less than 50, None if the sum of the two numbers is
more than or equal to 50
'''

def summ_num():
    num_one = int(input("Input first number: "))
    num_two = int(input("Input second number: "))
    if num_one + num_two < 50:
        print('The summ of two numbers is:',num_one + num_two)  
    elif num_one + num_two >= 50:
        print(None)
summ_num()    

'''
Puzzle 3
Define a function sum_even that takes one parameter:
When called, the function should return the sum of even integers in the list.
'''

def summ_list():
    counter = 0
    input_list = [int(x) for x in input('Print list of numbers: ').split()]
    for x in input_list:
        counter = counter + x
    print(counter)
summ_list() 

'''
Puzzle 4
Define a function remove_vowels that takes one parameter:
When called, the function should return a new string with all the vowels removed.
'''

import re
def remove_vowels():
    string = input("Type your string here: ")
    string_wo_vowels = re.sub("a|e|u|o|i","",string)
    print(string_wo_vowels)
remove_vowels()


'''
Puzzle 5
Define a function get_logest_string that takes one parameter:
When called, the function should return the longest string in the list. If there are ties, return the string that appears first in the list.
'''

def get_longest_string():
    input_string = list(map(str,input("Enter a list of words separated by space ").strip().split()))
    input_string.sort(key=len)
    if len(input_string) < 2:
        largest_string = input_string[-1]
    elif len(input_string[-1]) == len(input_string[-2]):
        largest_string = input_string[-2]
    else:            
        largest_string = input_string[-1]
    print(largest_string)     
get_longest_string() 

'''
Puzzle 6
Define a function that takes a list of integers
When called, the function should return a reversed list of the elements
'''

def reverse_list():
    input_list = list(map(int,input("Enter a list of elements: ").strip().split()))
    reverse_list = input_list[::-1]
    print(reverse_list)
reverse_list()

'''
Puzzle 7
Define a function that takes a list of variables
When called, the function should filter digits and return only strings 
'''

def filter_str():
    data = list(map(str,input("Type the text to filter: ").strip().split()))
    for x in data:
        if x.isdigit():
            data.remove(x)
    print(data)
filter_str()

'''
Puzzle 8
Define a function that takes one parameter.
When called, the function should return a morse code equivalent of the input string.
The function should meet the following:
- A space should be used between each morse code letter
- If space is encountered in the input string, it should be translated to forward slash
- The function should support upper and lowercase letters
'''

def morse_code():
    morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    translated = []
    data = input("Type text to translate to morse code: ").upper()
    for x in data:
        if x == " ":
            translated.append("/")
        elif x in morse_dict.keys():
            a = morse_dict.get(x)
            translated.append(a)
    morse_string = " ".join(str(x) for x in translated)
    print(morse_string)
morse_code()    

'''
Puzzle 9
Define a function that takes a list of integers.
When called, the function should return a second largest number in the list. If there is no second largest number, it should return None.
'''

def second_largest():
    input_nums = list(map(int, input("Type a list of numbers: ").strip().split()))
    input_nums.sort()
    if len(input_nums) < 2:
        print("None")
    else:
        second_largest = input_nums[-2]
        print(second_largest)    
second_largest()  

'''
Puzzle 10
Define a function that takes an integer.
When called, the function should return a string representation of the number with commas as thousand separator.
'''

def format_number_with_commas():
    input_num = int(input("Type a number: "))
    print(str(format(input_num, ',d')))
format_number_with_commas()       

'''
Puzzle 11
Define a function that takes a string and coverts it to ASCII code.
'''

def string_to_ascii():
    converted = []
    input_str = str(input("Type a text to convert to ascii: "))
    for x in input_str:
        converted.append(ord(x))
    print(converted)
string_to_ascii() 

'''
Puzzle 12
Define a function that takes a list of strings and returns a new list with all the strings that have at least  one vowel.
'''

def get_string_with_vowels():
    vowels = ["a", "e", "u", "o", "i"]
    input_list = list(map(str, input("Please type a list of words, separated by spaces: ").strip().split()))
    output_list = []
    for x in input_list:
        for y in x:
            if y in vowels:
                output_list.append(x)
                break
    print(output_list)
get_string_with_vowels()

'''
Puzzle 13
Define a function that takes an input of ten integers and returns a list with the first five elements reversed. The solution should use the slicing
insted of loops.
'''

def reverse_first_five_elements():
    input_nums = list(map(int, input("Please type at least ten numbers, separated by commas: ").strip().split(",")))
    if len(input_nums) < 10:
        print("The total list of numbers is less than ten")
        return
    else:
        input_nums[0:5] = reversed(input_nums[0:5])
    print(input_nums)
reverse_first_five_elements()

'''
Puzzle 14
Define a function that takes a string list as an input. When called, the function should return a list of words that are palindromes.
'''

def filter_palindromes():
    input_list = list(map(str, input("Please type a list of words, seprated by spaces: ").strip().split()))
    output_list = []
    for x in input_list:
        if x == x[::-1]:
            output_list.append(x)
    print(output_list)        
filter_palindromes() 


