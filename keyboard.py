import convert

# Task 2
# create a list of user input float numbers
# input: None
# output: a list of user input float numbers
def gather_numbers() -> list[float]:
    num_list = []
    repeat = 1
    while repeat == 1:
        user_input = input("Enter a number or type done to return list: ")
        if user_input == "done" or user_input == "Done" or user_input == "DONE":
            repeat = 0
        else:
            num = convert.str_to_float(user_input)
            num_list.append(num)
    num_list = [num for num in num_list if num is not None]
    return num_list

if __name__ == '__main__':
    num_list = gather_numbers()
    num_list_sum = 0
    for i in range(len(num_list)):
        num_list_sum = num_list_sum + num_list[i]
    print(num_list_sum)
