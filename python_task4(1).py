def student_data(student_name,student_id,student_marks):
    print(f'student_name = {student_name}')
    print(f'student_id = {student_id}')
    print(f'student_marks = {student_marks}')

    return{
        'studentname' : student_name,
        'studebtid' : student_id,
        'studentmarks' : student_marks
    }

student1=student_data('abc',19,300)
print()
print(f'student1 = {student1}')
print()

student2=student_data('pqr',17,289)
print()
print(f'student2 = {student2}')
print()
     
student3=student_data('xyz',18,250)
print()
print(f'student3 = {student3}')
print()