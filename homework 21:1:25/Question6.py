class Student():
    def __init__(self, name, age, gradeLevel):
        self.name = name
        self.age = age
        self.gradeLevel = gradeLevel

    def study(self):
        print(f"{self.name} is studying.")

    
class GradStudent(Student):
    def __init__(self, name, age, gradeLevel, thesisTitle):
        super().__init__(name, age, gradeLevel)
        self.thesisTitle = thesisTitle
    
    def research(self):
        print(f"{self.name} is researching for their thesis: {self.thesisTitle}")

cat = Student("Cat", 2, 0)
cat.study()

bird = GradStudent("Birdy", 1, 50, "exobiology" )
bird.research()