# Task 1
# convert a string to a float
# input: a string
# output: a float value if the given string represents a float value
def str_to_float(string:str):
    try:
        value = float(string)
        return value
    except ValueError as e:
        print(e)
