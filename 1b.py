class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

# Tworzenie dwóch przykładowych obiektów klasy Student
student1 = Student("Martyna", [70, 75, 80, 90])
student2 = Student("Dawid", [20, 30, 60, 45])

# Wywoływanie metody is_passed dla obiektów
result1 = student1.is_passed()
result2 = student2.is_passed()

# Wyświetlanie wyników
print(f"{student1.name} passed: {result1}")
print(f"{student2.name} passed: {result2}")