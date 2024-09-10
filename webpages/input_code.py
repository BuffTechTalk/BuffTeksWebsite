# sample function without input arguments and return values
def print_hello():
    print('Hello WT!')

# type function name to call the function directly.
print_hello()
print_hello()
print_hello()
# sample function with input arguments and return value
def tree_sum(a,b,c):
    result = a+b+c
    return result

# call function with given values and use another variable to hold return values
sum1 = tree_sum(1,2,3)
sum2 = tree_sum(4,5,6)

print('sum1: ', sum1)
print('sum2: ', sum2)

# sample function with multiple return values
def sum_len(num_list):
    total = 0
    for num in num_list:
        total = total+num
    return total, len(num_list)

num_list = [0,1,2,3,4,5,6,7,8,9]
# t is a variable used to hold returned total
# l is a variable used to hold returned length: len(num_list)
t,l = sum_len(num_list)
print(f'The length of list is: {l}; the sum of list is: {t}')