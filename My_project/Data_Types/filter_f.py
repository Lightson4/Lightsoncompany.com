#filter of list
'''numbers = [1, 2, 3, 4, 5, 6, 8]
def is_even (x):
    return x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers)
'''
#filter with lambda
numbers = [1, 2, 3, 4, 5, 6, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)