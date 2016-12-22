# coding: utf-8
def find_min_index(number_list):
    min_index = 0
    min_value = number_list[min_index]

    for i in range(1, len(number_list)):
        if(number_list[i] < min_value):
            min_index = i
            min_value = number_list[min_index]
    return min_index

question = [5, 3, 2, 8, 9, 0, 4, 1, 6, 7]

# sorting
for i in range(len(question)):

print(question)
