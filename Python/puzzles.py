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

'''
Puzzle 15
Define a function that takes a string list as an input. When called, the function should replace any "P","Y","T","H","O","N" letters with "X".
The function should be case insensitive.
'''

def censor_python():
    censor_list = ["P","Y","T","H","O","N","p","y","t","h","o","n"]
    censor_output = []
    input_str = str(input("please type the words, separated by spaces: ").strip().split())
    for x in input_str:
        for y in x:
            if y in censor_list:
                censor_output.append("X")
            else:
                censor_output.append(y)
    str_output = ''.join(str(x) for x in censor_output)
    print(str_output)
censor_python()   

'''
Puzzle 16
A string is happy if every three consecutive characters are distinct. Examples of happy strings:
"abcdefg"
"qwerty"
Examples of unhappy strings:
"aaaaaa"
"cbc"
"hello"
Define a function that takes an input string. The function should return a bool indicatin if the string is happy or not.
'''

def check_if_string_is_happy():
    input_str = str(input("Type a string to check: "))
    n = 0
    m = 3
    if len(input_str) < 3:
        return True
    else:
        for i in range(len(input_str)):
            checked_part_of_str = input_str[n:m]
            if len(set(checked_part_of_str)) != len(checked_part_of_str):
# set function returns a unique set of characters from a string(part of the string in our case). if the length of set will be equal to the length of the original part of the string 
# we are good. If not - we are unhappy.                
                return False
                break
            else:
                n = n + 1
                m = m + 1
        return True        
print(check_if_string_is_happy())  

'''
Puzzle 17
Define a function, when called, the function should return the number of digits in the input_num. The function should be recursive. The function should
not convert the integer to a string.
'''
# Make a function call by dividing the number by 10, reducing the input size of the given number by 1, and adding 1 for this operation.
def get_number_of_digits(input_num):
    if input_num // 10 == 0:
        return 1
    return 1 + get_number_of_digits(input_num // 10)
print(get_number_of_digits(input_num = 9))  

'''
Puzzle 18
Define a function, that takes one parameter(the board list of tic tac toe). The function should determine if X or O has won. If there is a draw, the function
should return None.
'''
def get_tic_tac_toe_winner():
    tic_tac_toe_list = ["","X","O"]
    tic_tac_toe_str = ""
    input_board = list(map(str, input("Please enter the tic tac toe board: ").upper().strip().split()))
    print(input_board)
# Iterating over each symbol in the input board and coverting them to a string    
    for x in input_board:
        for y in x:
            if y in tic_tac_toe_list:
                tic_tac_toe_str = tic_tac_toe_str + str(y)
# Checking all possible variants for X to win                 
    if tic_tac_toe_str[0:3].count("X") == 3:
        winnerX = "X"
    elif tic_tac_toe_str[3:6].count("X") == 3:
        winnerX = "X"
    elif tic_tac_toe_str[6:9].count("X") == 3:
        winnerX = "X"
    elif tic_tac_toe_str[0:8:3].count("X") == 3:
        winnerX = "X"
    elif tic_tac_toe_str[1:9:3].count("X") == 3:
        winnerX = "X"
    elif tic_tac_toe_str[2:10:3].count("X") == 3:
        winnerX = "X"
    elif tic_tac_toe_str[0:10:4].count("X") == 3:
        winnerX = "X" 
    elif tic_tac_toe_str[2:8:2].count("X") == 3:
        winnerX = "X"
# Checking all possible variants for O to win        
    if tic_tac_toe_str[0:3].count("O") == 3:
        winnerO = "O"
    elif tic_tac_toe_str[3:6].count("O") == 3:
        winnerO = "O"
    elif tic_tac_toe_str[6:9].count("O") == 3:
        winnerO = "O"
    elif tic_tac_toe_str[0:8:3].count("O") == 3:
        winnerO = "O"
    elif tic_tac_toe_str[1:9:3].count("O") == 3:
        winnerO = "O"
    elif tic_tac_toe_str[2:10:3].count("O") == 3:
        winnerO = "O"
    elif tic_tac_toe_str[0:10:4].count("O") == 3:
        winnerO = "O" 
    elif tic_tac_toe_str[2:8:2].count("O") == 3:
        winnerO = "O"
# If both X and O are winners, we print None        
    if len(winnerX) == len(winnerO):
        print("None")
    elif len(winnerX) > len(winnerO):
        print(winnerX)
    else:
        print(winnerO)
get_tic_tac_toe_winner() 

'''
Puzzle 19
Define a function print_triangle, which takes two parameters:
number of levels: int
symbol: str
When called, the function should output a centered triangle shape made up of the desired symbol.
The number of symbols in each row should increase by two with each level.
'''
def print_triangle():
    number_of_levels = int(input("Pleas enter a number of levels in the triangle: "))
    symbol = str(input("Please enter a symbol, which will be used to build the triangle: "))
    n = 1
    for x in range(number_of_levels):
        string = "" * n + symbol * n
        n = n + 2
        print(string.center(number_of_levels + number_of_levels))
print_triangle()  
