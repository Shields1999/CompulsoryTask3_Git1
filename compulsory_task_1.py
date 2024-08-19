# create Class and Sub-Class
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    location = "Cape Town"

    def contact_details(self):
        print(f'''\nPlease contact us by visiting {self.contact_website}''')
        
    def location(self):
        print(f'''\nOur Head Office is based in {self.location}''')

class OOPCourse(Course):
    
    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"
    course_id = "#12345"
        
    def trainer_details(self):
        print(f'''\nThis course is the {self.name} which focuses
on {self.description} lead by {self.trainer}''')
        
    def show_course_id(self):
        print(f"\nThe ID for the course is: {self.course_id}")
        

course_1 = OOPCourse()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

