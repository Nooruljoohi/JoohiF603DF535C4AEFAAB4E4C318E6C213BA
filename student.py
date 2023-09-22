class Student:
  def __init__(self,name,roll_number,
                   cgpa):
   self.name = name
   self.roll_number = roll_number
   self.cgpa=cgpa 


def sort_students(student_list):
 
   sorted_student = sorted                   (student_list,key=lambda student: student.cgpa,reverse=True) 
   return sorted_student
 
students = [
  Student("Joo","231",9.6),
  Student("Shiva","232",8.8),
  Student("Dev","233",8.5),
]  
sorted_students=sort_students(students)

for student in sorted_students:
  print("Name: {},Number: {},Cgpa:{}".format (student.name,student.roll_number,student.cgpa))


