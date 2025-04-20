def calculate_gpa(marks_list):
    if not marks_list:
        return 0
    return sum(marks_list) / len(marks_list)
