participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1, group2, separator=','):

    surname_first_group = group1.split(separator)
    surname_second_group = group2.split(separator)

    set_first_group = set(surname_first_group)
    set_second_group = set(surname_second_group)

    general_participants = set_first_group.intersection(set_second_group)
    result = sorted(list(general_participants))

    return result


print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
