total_class = int(input("Enter the total number of class : "))
class_attended =  int(input("Enter the number of class attended : "))

percentage = (class_attended / total_class) * 100

if percentage < 75:
    print("Student does not allowed to sit in the exam")
else:
    print("Student allowed to sit in the exam")