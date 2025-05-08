#class vaiables in python 
class Students:
    class_year = 2025
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.num_students +=1
student1 = Students("Kupakwashe", 20)
student2 = Students("Gwavava", 19)
student3 = Students("Chimuti", 34)
student4 = Students("Chitereki", 60)

# print(student1.name)
# print(student1.age)
# print(Students.class_year)
print(f"My graduating class of {Students.class_year} has {Students.num_students} students, these includes:")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)