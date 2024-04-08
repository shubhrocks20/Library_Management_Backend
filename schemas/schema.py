def student_helper(student) -> dict:
    return {
       
        "name": student["name"],
        "age": student["age"],
       
    }

def singleStudent(student) -> dict:
    return {
        "name": student["name"],
        "age": student["age"],
        "address": student["address"]
    }
def list_students(students)->list:
    return [student_helper(student) for student in students]