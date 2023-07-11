numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_number = 4
total = sum(numbers[:missing_number]) + sum(numbers[missing_number+1:])
count = len(numbers)
numbers[missing_number] = total / count  # TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
