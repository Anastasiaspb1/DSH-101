def find_common_participants(str1, str2, delimiter=','):
    list1 = set(str1.split(delimiter))
    list2 = str2.split(delimiter)
    common_participants = list(list1.intersection(list2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
