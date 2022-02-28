class Students:
    def __init__(self,name,first_name,age):
        self.name=name
        self.first_name=first_name
        self.age=age
    def get_name(self):
        return self.name
    def get_first_name(self):
        return self.first_name
    def get_age(self):
        return self.age
    def set_name(self,new_name):
        self.name=new_name
    def set_first_name(self,new_first_name):
        self.first_name=new_first_name

class Sinf:
    def __init__(self,sinf_soni):
        self.sinf_soni=sinf_soni
        self.students=[]
        self.class_mates=0
    def get_sinf_soni(self):
        return self.sinf_soni
    def get_students(self,yosh):
        tmp=[]
        for oquvchi in self.students:
            if oquvchi.age>=yosh:
                tmp.append(oquvchi)
        return tmp
    def get_class_mates(self):
        return self.class_mates
    def add_students(self,students):
        self.students.append(students)
        self.class_mates+=1

student1=Students("Ubaydullo","Usmonov",14)
student2=Students("Imron","Zokirov",13)
student3=Students("Abduraxmon","Abduvositov",12)
student4=Students("Jamshid","Rajabov",15)
student5=Students("Abdujalil","Hamidullaye",15)
student6=Students("Ubaydullo","Usmonov",10)
student7=Students("Imron","Zokirov",9)
student8=Students("Abduraxmon","Abduvositov",11)
student9=Students("Jamshid","Rajabov",5)
student10=Students("Abdujalil","Hamidullaye",10)
sinf=Sinf("Biologiya sinifi")

sinf.add_students(student1)
sinf.add_students(student2)
sinf.add_students(student3)
sinf.add_students(student4)
sinf.add_students(student5)
sinf.add_students(student6)
sinf.add_students(student7)
sinf.add_students(student8)
sinf.add_students(student9)
sinf.add_students(student10)

print(sinf.get_sinf_soni())
for student in sinf.get_students(13):
    print(student.name,student.first_name,student.age)
print(sinf.get_class_mates())
