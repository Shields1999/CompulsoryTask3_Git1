# create Class and Sub-Class
class Course:
    #name, contact_website can be changed to suit
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    location = "Cape Town"

    def contact_details(self):
        print(f'''
Please contact us by visiting {self.contact_website}''')
        
    def location(self):
        print(f'''
Our Head Office is based in {self.location}''')

#Create Sub-Class
class OOPCourse(Course):
    
    #description, trainer and course_id can be changed to suit
    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"
    course_id = "#12345"
        
    def trainer_details(self):
        print(f'''
This course is the {self.name} which focuses
on {self.description} lead by {self.trainer}''')
        
    def show_course_id(self):
        print(f"The ID for the course is: {self.course_id}\n")
        
#Displays course defaults inside terminal
course_1 = OOPCourse()

#Displays course specific information inside terminal
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

