class ComEnStudent:
    def __init__(self, name, courses, content=""):
        self.name = name
        self.courses_ids = courses
        self.content = content
    def take_courses(self, *courses):
        list_course = self.courses_ids
        for i in courses:
            list_course.append(i)
        self.courses_ids = list_course
    def make_content_type(self, content):
        self.content = content
    def __str__(self):
        return f"{self.name} has taken these courses: {self.courses_ids}"

class CoEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)
            
class DMEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)
    def __str__(self):
        if self.content == "":
            return f"{self.name} has taken these courses: {self.courses_ids}"
        else:
            return f"{self.name} has taken these courses: {self.courses_ids} \n specialized in creating content type:{self.content}"

if __name__ == "__main__":
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("SC401206")
        print(com_student)
