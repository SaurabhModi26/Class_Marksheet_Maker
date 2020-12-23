class student :
    school="Sakar English School"
    saddress="New C.G. Road"
    
    def __init__(self,name_inp,roll_inp,m1_inp,m2_inp) :
        self.name=name_inp
        self.roll=roll_inp
        self.m1=m1_inp
        self.m2=m2_inp
    
    def show(self) :
        return f"\nName : {self.name}\nRoll : {self.roll}\nMarks1 : {self.m1}\nMarks2 : {self.m2}"
    def avg(self) :
        average=(self.m1+self.m2)/2
        return "Average : "+str(average)
    
    def printstud(self) :
        print(self.topic()) 
        print(self.show())
        print(student.school_show())
        print(student.saddress_show())
        print(self.avg())
    
    @classmethod
    def school_show(cls) :
        return "School : " + str(cls.school)
    
    @classmethod
    def saddress_show(cls) :
        return "SchoolAddress : " +str(cls.saddress)
    
    @staticmethod
    def topic() :
        return "\nStudent credentials : "
   
n=int(input("Enter number of students : "))

s=[]
for i in range(1,n+1) :
    s.append(f"s{i}")
    print(f"\nFor student {i} : ")
    name_loop=input("Enter name :")
    roll_loop=input("Enter roll : ")
    m1_loop=int(input("Enter m1 : "))
    m2_loop=int(input("Enter m2 : "))
    
    s[i-1]=student(name_loop,roll_loop,m1_loop,m2_loop)
    
print("\n-----------------------------Class marksheet--------------------------\n")
for i in range(1,n+1) :
    s[i-1].printstud()
print("\n----------------------------------------------------------------------\n")