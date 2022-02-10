class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Tell(self):
        print(f'my name is {self.name},I am {self.age}')

    def Study(self,subject):
        print(f'my name is{self.name},I love '+subject+' haha')

class postStudent(Student):
     def __init__(self,name,age,heigh):
         super().__init__(name,age)
         self.heigh=heigh

     def Study(self, subject,major):
         print(f'{self.name}  {self.age} {self.heigh} +"my favourate subject"+{subject}+" major is "+{major}')


stu1=Student('xinhao',18)
stu1.Tell()
stu1.Study('java')
print(f'{stu1.age}   {stu1.name}')
print("---------------")
stu2=postStudent('haohao',22,185)
stu2.Study('python','ttt')

print('子类调用父类的方法')
super(postStudent,stu2).Study('c++')