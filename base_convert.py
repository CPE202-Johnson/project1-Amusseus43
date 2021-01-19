import math

#dictionary to use for numbers with base higher than 10
number_dict = {
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}

# int(number in base 10, changed base) -> string
# returns a string of the number in a different base
def convert(num, b):
    if b <=16:
        # uses run_convert function for recursive work
        string_a =  run_convert(num,b)
        # if loop used to check for special case when number is 0
        if string_a == "":
            return "0"
        else:
            return string_a

# int(number and base) -> string
# changes the number from base 10 to a sepcified base between 2 to 16
def run_convert(num,b):
    """Recursive function that returns a string representing num in the base b"""
    if num==0:
        return ""
    next_num = num//b
    if b> 10 and (num%b)>=10:
        temp_remainder = number_dict[num%b]
    else:
        temp_remainder = num % b
    return run_convert(next_num,b) + str(temp_remainder)


