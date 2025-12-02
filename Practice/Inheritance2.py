class student:
    student_id= 10
    student_name="abubakar"
    student_class= 9
    def m1(self):
        print(self.student_id,self.student_name,self.student_class)

class studentdetail(student):
    student_marks = 950
    def m2(self):
        self.a=5
        self.b=10
        print(self.a + self.b)

objb= studentdetail()
print(objb.student_id)
print(objb.student_name)
print(objb.student_class)

objb.m2()
print(objb.a)
print(objb.b)


