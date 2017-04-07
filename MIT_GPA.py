#Author: Karleigh Moore
#Disclaimer: I made this for fun/for those "how well do I have to do to have a GPA of X" moments
#Use as you wish, but trust the registrar more than this
#This currently does not round as the registrar does

class Course:
    def __init__(self, name, grade, units, semester, technical):
        self.name = name #string
        self.grade = grade #integer A=5, B=4, C=3, D=2, F=1
        self.units = units #integer
        self.semester = semester #string
        self.technical = technical #boolean

class Transcript:
    def __init__(self):
        self.courses = []

    def add(self, course_name, grade, units, semester, technical):
        course = Course(course_name, grade, units, semester, technical)
        self.courses.append(course)

    def get_total_gpa(self):
        total_units = 0.0
        grade_map = {"A":0, "B":0, "C":0, "D":0, "F":0} #maps units to grades
        for course in self.courses:
            total_units += course.units
            if course.grade == 5:
                grade_map["A"] += (5*course.units)
            elif course.grade == 4:
                grade_map["B"] += (4*course.units)
            elif course.grade == 3:
                grade_map["C"] += (3*course.units)
            elif course.grade == 2:
                grade_map["D"] += (2*course.units)
            else:
                grade_map["F"] += (1*course.units)
        
        denom = sum(grade_map.values())

        return denom/total_units

    def get_total_gpa_filter(self, courses):
        total_units = 0.0
        grade_map = {"A":0, "B":0, "C":0, "D":0, "F":0} #maps units to grades
        for course in courses:
            total_units += course.units
            if course.grade == 5:
                grade_map["A"] += (5*course.units)
            elif course.grade == 4:
                grade_map["B"] += (4*course.units)
            elif course.grade == 3:
                grade_map["C"] += (3*course.units)
            elif course.grade == 2:
                grade_map["D"] += (2*course.units)
            else:
                 grade_map["F"] += (1*course.units)
        
        denom = sum(grade_map.values())

        return denom/total_units

    def get_semester_gpa(self, semesters, techOnly): #takes in a list of semesters to include
        filtered_courses = []
        for course in self.courses:
            if course.semester in semesters:
                if techOnly:
                    if course.technical:
                        filtered_courses.append(course)
                else:
                    filtered_courses.append(course)
        return self.get_total_gpa_filter(filtered_courses)

    def get_overall_tech_gpa(self):
        filtered_courses = []
        for course in self.courses:
            if course.technical:
                filtered_courses.append(course)
        return self.get_total_gpa_filter(filtered_courses)

#make a transcript by adding courses like so
transcript = Transcript()
transcript.add("7.013", 5, 12, "s13", False)

#can print out various types of GPAs
print("Overall GPA (S13 to F16):", transcript.get_total_gpa())

print("Technical GPA (S13 to F16):", transcript.get_overall_tech_gpa())

print("Technical GPA last 3 semesters (F16, S16, F15):", transcript.get_semester_gpa(["f16","f15","s16"], True))

print("Technical GPA lowest semester (F14) dropped:", transcript.get_semester_gpa(["f16","f15","s16", "f13", "s13", "s14", "s15"], True), "\n")


