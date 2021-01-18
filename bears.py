# int -> boolean
# returns True if its posssible to win the bear game(win if you can end up with exactly 42 bears)
def bears(n):
    ''' 
    1. If n is even, then you may give back n/2 bears.
    2. If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
    3. If n is divisible by 5, then you may give back 42 bears.
    '''
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0 and bears(n/2):
        return True
    if n % 5 == 0 and bears(n-42):
        return True
    if n % 3 == 0 or n % 4 == 0:
        last_digit = n%10
        first_digit = (n%100 - last_digit)/10
        return_second_rule = first_digit * last_digit
        return return_second_rule > 0 and bears(n- return_second_rule)
    return False



print(bears(41))











