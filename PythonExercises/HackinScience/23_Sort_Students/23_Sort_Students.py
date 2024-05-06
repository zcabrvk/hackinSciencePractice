students = [(85, "Susan Maddox"), (6, "Joshua Tran"), (37, "Jeanette Wafer")]


def sort_by_mark(list):
    return sorted(list, key= lambda student: student[0], reverse=True)


def sort_by_name(list):
    return sorted(list, key= lambda student: student[1])


print(sort_by_mark(students))

print(sort_by_name(students))