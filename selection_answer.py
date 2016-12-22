# coding: utf-8
question = [5, 3, 2, 8, 9, 0, 4, 1, 6, 7]

min_index = 0
min_value = question[min_index]

for i in range(1, len(question)):
    if(question[i] < min_value):
        min_index = i
        min_value = question[min_index]
print(min_value)
print(min_index)
