# coding: utf-8
def find_min_value(number_list):
    min_index = 0
    min_value = question[min_index]

    for i in range(1, len(question)):
        if(question[i] < min_value):
            min_index = i
            min_value = question[min_index]
    return min_value

question = [5, 3, 2, 8, 9, 0, 4, 1, 6, 7]

answer = []

for i in range(len(question)):
    answer.append(find_min_value)
    

    for i in range(1, len(question)):
        if(question[i] < min_value):
            min_index = i
            min_value = question[min_index]

print(min_value)
print(min_index)
