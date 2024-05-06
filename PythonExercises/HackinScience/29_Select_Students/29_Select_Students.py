def select_student(my_class, minGrade):
    accepted = []
    rejected = []

    for student in my_class:
        if(student[1] >= minGrade):
            accepted.append(student)
        else:
            rejected.append(student)
    return {
        "Accepted": accepted,
        "Rejected": rejected
    }

my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]

print(select_student(my_class, 20))