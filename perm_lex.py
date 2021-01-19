# string -> list(of strings) (if string has n characters then list should have n! permutations)
# take a string and return all possible permutations of the string in dictionary order
def perm_gen_lex(string): 
    ''' input is given as a string of 0 or more unique lower-case alphabets in order '''
    string_list = [] # list to hold all possible permutations
    if len(string) == 1:
        return [string] # returns the singular character inside of a list
    for n in string:
        front_char = n
        temp_string = string.replace(n,"")
        temp_list = perm_gen_lex(temp_string)

        # adding front char to each permutation
        for x in range(len(temp_list)):
            temp_list[x] = front_char + temp_list[x]
        string_list = string_list + temp_list
    return string_list    

