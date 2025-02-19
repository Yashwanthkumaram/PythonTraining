student_map = {

}

class Subjects:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
        pass

    pass


class Semester:
    def __init__(self,subjects):
        self.subjects  = subjects
        pass

    pass

class Student:
    def __init__(self, name , usn , sem_map):
        if student_map.__contains__(usn):
            raise Exception("USN must unique")
        student_map[usn] = self
        self.name = name
        self.name = usn
        self.sem_map = sem_map
        pass

    def get_sem_marks(self,sem=None):
            if sem==None:
                semester  = list(self.sem_map)[-1]
                for marks in semester.subjects:
                    print(f"{marks.name} : {marks.marks}")
            else:
                for semester in self.sem_map:
                    if(semester==sem):
                        for marks in semester.subjects:
                            print(f"{marks.name} : {marks.marks}")

    pass

def get_sem_marks(usn,sem=None):
        print(usn)
        if student_map.__contains__(usn):
            if sem==None:
                semester  = list(student_map[usn].sem_map)[-1]
                for marks in semester.subjects:
                    print(f"{marks.name} : {marks.marks}")
            else:
                for semester in student_map[usn].sem_map:
                    if(semester==sem):
                        for marks in semester.subjects:
                            print(f"{marks.name} : {marks.marks}")
        else:
            raise Exception(f"There exist No student with that {usn}")


maths = Subjects("maths",87)
physics = Subjects("physics", 97)
chemistry = Subjects("chemistry",67)


dsa = Subjects("dsa",67)
daa = Subjects("daa", 47)
java = Subjects("java",77)

sem1 = Semester([maths,physics,chemistry])
sem2 = Semester([java,daa,java])

semMap ={
    sem1 : sem1,
    sem2 : sem2
}

yashwanth = Student("yashwanth", "4VV21Ci061", semMap)

#get grades of particular semester
yashwanth.get_sem_marks()

#get grades of current semester
yashwanth.get_sem_marks(sem1)

#get funtion outside class
get_sem_marks("4VV21Ci061",sem1)


