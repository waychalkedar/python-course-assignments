numbers = [1203, 1256, 312456, 98]

numbers_as_string = [str(number) for number in numbers]
print(numbers_as_string)
print(''.join(numbers_as_string))
numbers_as_list = list(''.join(numbers_as_string))
print(numbers_as_list)

for num in range(10):
    print(f"{num} {numbers_as_list.count(str(num))}")