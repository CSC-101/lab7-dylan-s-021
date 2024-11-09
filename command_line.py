import sys
import convert

# Task 3

if __name__ == '__main__':
    print(sys.argv)
    num_list = []
    num_list_sum = 0
    for i in range(len(sys.argv)):
        num = convert.str_to_float(sys.argv[i])
        if num is not None:
            num_list.append(num)
    for j in range(len(num_list)):
        num_list_sum = num_list_sum + num_list[j]
    print(num_list_sum)
