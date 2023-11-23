class StudentMarks:

    def __init__(self, name, rno, m1, m2, m3):
        self.name = name
        self.rno = rno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def details(self):
        average_marks = (self.m1 + self.m2 + self.m3) / 3
        if average_marks >= 50:
            return "pass"
        else:
            return "fail"

temp = StudentMarks("aryan", 2, 50, 60, 70)
result = temp.details()
print(f"The result for {temp.name} with roll number {temp.rno} with marks {temp.m1},{temp.m2},{temp.m3} is {result}")
