# coding: utf-8
def find_min_index(number_list):
    min_index = 0
    min_value = question[min_index]

    for i in range(1, len(question)):
        if(question[i] < min_value):
            min_index = i
            min_value = question[min_index]
    return min_index

question = [5, 3, 2, 8, 9, 0, 4, 1, 6, 7]

answer = []

# sorting
number_of_data = len(question)
for i in range(number_of_data):
    min_index = find_min_index(question)
    answer.append(question[min_index])
    del(question[min_index])

print(answer)