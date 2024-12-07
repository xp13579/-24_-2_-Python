# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, arg=","):
    first_group = str_1.split(arg)
    second_group = str_2.split(arg)
    common_participants = list(set(first_group).intersection(second_group))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, arg="|"))