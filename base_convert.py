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
# int(number in base 10, changed base) -> int(number in different base)
# changes the number from base 10 to a sepcified base between 2 to 16
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if num==0:
        return ""
    next_num = math.floor(num/b)
    if b> 10 and (num%b)>=10:
        temp_remainder = number_dict[num%b]
    else:
        temp_remainder = num % b
    return convert(next_num,b) + str(temp_remainder)

print(number_dict[10])
print(convert(45,2))
print(convert(30,4))
print(convert(316,16))