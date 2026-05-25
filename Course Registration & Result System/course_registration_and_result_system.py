## Creating the first class Student here with display and update info methods
class Student:
    def __init__(self,student_id,name,email,phone):
        self.student_id=student_id
        self.name=name
        self.email=email
        self.phone=phone
    def display(self):
        print(f"{self.student_id}\t\t{self.name}\t\t{self.email}\t\t{self.phone}")
    def update_info(self,email,phone):
        self.email=email
        self.phone=phone

## creating the second class named Course
class Course:
    def __init__(self,course_id,title,credit_points):
        self.course_id=course_id
        self.title=title
        self.credit_points=credit_points
    def display(self):
        print(f"{self.course_id}\t\t{self.title}\t\t{self.credit_points}")

## creating the third class as enrollment
class Enrollment:
    def __init__(self,enrollment_id,student_id,course_id):
        self.enrollment_id=enrollment_id
        self.student_id=student_id
        self.course_id=course_id
    def display(self):
        print(f"{self.enrollment_id}\t\t{self.student_id}\t\t{self.course_id}")

## creating another class as result
class Result:
    def __init__(self,result_id,enrollment_id,score):
        self.result_id=result_id
        self.enrollment_id=enrollment_id
        self.score=score
        self.grade=self.calculate_grade()
    def calculate_grade(self):
        if self.score>=80:
            return"Higher Dinstinction(HD)"
        elif self.score>=70:
            return"Distinction(D)"
        elif self.score>=60:
            return"Credit(C)"
        elif self.score>=50:
            return"Pass(P)"
        elif self.score>=40:
            return"Marginal Fail(MM/PC)"
        else:
            return"Fail(N)"

## Now lets add CCRS_Files_Manager as a class to manage the txt files that i have made to store data in the files 
class CCRS_Files_Manager:
    def __init__(self):
        self.students=[]
        self.courses=[]
        self.enrollments=[]
        self.results=[]
        self.load_all()

## creating the methods to load data from files also initializing them
    def load_all(self):
        self.load_students()
        self.load_courses()
        self.load_enrollments()
        self.load_results()
    def log(self,message):
        with open("system_log.txt","a") as f:
            f.write(message+"\n")

 ## now creating methods to read data from files line by line and loading them
    def load_students(self):
        try:
            with open("students.txt","r")as f:
                for line in f:
                    line = line.strip()
                    if line and "Student ID:" not in line:
                        s=line.split(",")
                        if len(s) == 4:
                            self.students.append(Student(*s))
        except FileNotFoundError:
            print("File not found:students.txt")
            open("students.txt","w")

    def load_courses(self):
        try:
            with open("courses.txt","r")as f:
                for line in f:
                    line = line.strip()
                    if line and "Course ID:" not in line:
                        c=line.split(",")
                        if len(c) == 3:
                            self.courses.append(Course(c[0],c[1],c[2]))
        except FileNotFoundError:
            print("File not found:courses.txt")
            open("courses.txt","w")

    def load_enrollments(self):
        try:
            with open("enrollments.txt","r")as f:
                for line in f:
                    line = line.strip()
                    if line and "Enrollment ID:" not in line:
                        e=line.split(",")
                        if len(e) == 3:
                            self.enrollments.append(Enrollment(*e))
        except FileNotFoundError:
            print("File not found:enrollments.txt")
            open("enrollments.txt","w")

    def load_results(self):
        try:
            with open("results.txt","r")as f:
                for line in f:
                    line = line.strip()
                    if line and "Score:" not in line:
                        r=line.split(",")
                        if len(r) >= 3:
                            self.results.append(Result(r[0],r[1],int(r[2])))
        except FileNotFoundError:
            print("File not found:results.txt")
            open("results.txt","w")

 ## now creating methods to save the data in the files 
    def save_students(self):
        with open("students.txt","w")as f:
            for s in self.students:
                f.write(f"{s.student_id},{s.name},{s.email},{s.phone}\n")

    def save_courses(self):
        with open("courses.txt","w")as f:
            for c in self.courses:
                f.write(f"{c.course_id},{c.title},{c.credit_points}\n")

    def save_enrollments(self):
        with open("enrollments.txt","w")as f:
            for e in self.enrollments:
                f.write(f"{e.enrollment_id},{e.student_id},{e.course_id}\n")

    def save_results(self):
        with open("results.txt","w")as f:
            for r in self.results:
                f.write(f"{r.result_id},{r.enrollment_id},{r.score},{r.grade}\n")

## Now making this thing operate with functions to add the input given by user and save in the files
    def add_student(self):
        s_id=input("Student ID:")
        if not s_id:
            print("Invalid ID")
            return
        name=input("Name:")
        email=input("Email:")
        phone=input("phone:")
        if not name or not email or not phone:
            print("Fields Missing.")
            return
        self.students.append(Student(s_id,name,email,phone))
        self.save_students()
        self.log("Student Added")
        print("Student has been added successfully.")

    def add_course(self):
        c_id=input("Course ID:")
        if not c_id:
            print("Invalid ID")
            return
        title=input("Title:")
        credit=input("Credit:")
        if not title or not credit:
            print("Fields Missing.")
            return
        self.courses.append(Course(c_id,title,credit))
        self.save_courses()
        self.log("Course Added")
        print("Course has been added successfully.")

    def enroll_student(self):
        e_id=input("Enrollment ID:")
        s_id=input("Student ID:")
        c_id=input("Course ID:")
        for e in self.enrollments:
            if e.student_id==s_id and e.course_id==c_id:
                print("Repeated Enrollment.")
                return
        self.enrollments.append(Enrollment(e_id,s_id,c_id))
        self.save_enrollments()
        self.log("Student Enrolled")
        print("Enrollment of student is successful.")

    def add_result(self):
        r_id=input("Result ID:")
        e_id=input("Enrollment ID:")
        try:
            score=int(input("score(0-100):"))
            if score<0 or score>100:
                print("Score doesnot lie between 0-100")
                return
        except ValueError:
            print("Invalid score")
            return
        self.results.append(Result(r_id,e_id,score))
        self.save_results()
        self.log("Result added")
        print("Result is recorded successfully.")

    def view_transcript(self):
        s_id=input("Student ID:")
        student_exists=False
        for s in self.students:
            if s.student_id==s_id:
                student_exists=True
                break
        if not student_exists:
            print("Invalid ID")
            return
        print("Course_ID\t\tScore\t\tGrade")
        print("-" * 50)
        for e in self.enrollments:
            if e.student_id==s_id:
                for r in self.results:
                    if r.enrollment_id==e.enrollment_id:
                        print(e.course_id,"\t\t",r.score,"\t\t",r.grade)

    def update_student(self):
        print("1. Search student")
        print("2. Update student info")
        sub_choice=input("Choose option:")
        
        if sub_choice=="1":
            s_id=input("Enter Student ID to search:")
            student_found=False
            for s in self.students:
                if s.student_id==s_id:
                    student_found=True
                    print("\nStudent Found:")
                    print("Student_ID\t\tName\t\t\tEmail\t\t\tPhone")
                    print("-" * 60)
                    s.display()
                    break
            if not student_found:
                print("Invalid ID - Student not found.")
        
        elif sub_choice=="2":
            s_id=input("Student ID to update:")
            student_found=False
            for s in self.students:
                if s.student_id==s_id:
                    student_found=True
                    new_email=input("New Email:")
                    new_phone=input("New Phone:")
                    s.update_info(new_email,new_phone)
                    self.save_students()
                    self.log("Student Updated")
                    print("Student info updated successfully.")
                    break
            if not student_found:
                print("Invalid ID")
        else:
            print("Invalid option.")

    def list_courses(self):
        print("Course_ID\t\tTitle\t\t\tCredit_Points")
        print("-" * 60)
        for c in self.courses:
            c.display()

    def list_enrollments(self):
        print("Enrollment_ID\t\tStudent_ID\t\tCourse_ID")
        print("-" * 50)
        for e in self.enrollments:
            e.display()

## Creating a CLI menu so for better User experience 
def main():
    manager=CCRS_Files_Manager()
    while True:
        print("\n---Course Registration and Results---")
        print("1.Add student")
        print("2.Add course")
        print("3.Enroll student in a course")
        print("4.Add result")
        print("5.View student transcript")
        print("6.View course list")
        print("7.View enrollment list")
        print("8.Update student info")
        print("9.Exit")
        choice=input("Choose Option:")
        print("\n")
        if choice=="1":
            manager.add_student()
        elif choice=="2":
            manager.add_course()
        elif choice=="3":
            manager.enroll_student()
        elif choice=="4":
            manager.add_result()
        elif choice=="5":
            manager.view_transcript()
        elif choice=="6":
            manager.list_courses()
        elif choice=="7":
            manager.list_enrollments()
        elif choice=="8":
            manager.update_student()
        elif choice=="9":
            print("Exiting the system.")
            break
        else:
            print("Invalid option.")

## now this thing runs the main function if the file is to be executed directly here            
if __name__ == "__main__":
    main()
    