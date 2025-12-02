class school:
    def __init__(self,id,name,grades):
        self.id=id
        self.name=name
        self.grades=grades

    def displayresults(self,school):
        print ("id is:",    self.id)
        print("name is:",   self.name)
        print("grades are:",    self.grades)
        print("school name is :", school)


sc= school(1,"abubakar",9)
sc.displayresults("crescent")