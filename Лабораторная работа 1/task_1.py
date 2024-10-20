numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_element = numbers.index(None)

total_sum = sum(numbers[0:4]) + sum(numbers[5: ])

count = len(numbers)

average = total_sum / count

numbers[missing_element] = average

print("Измененный список:", numbers)

