import re # Python Library fro regular esapression
from Users.student import Student
from Users.teacher import Teacher

class EmailRegister:
    def __init__(self):
        self.student_manager = Student()
        self.teacher_manager = Teacher()
        
    def validate_email(self, email):
        """Validate email format using regex"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def classify_and_register_email(self, email):
        """Classify and register email based on domain"""
        if not self.validate_email(email):
            return False, "Invalid email format"

        if email.endswith("@estudiante.utv.edu.co"):
            self.student_manager.add_email(email)
            return True, "Student email registered successfully"
        elif email.endswith("@utv.edu.co"):
            self.teacher_manager.add_email(email)
            return True, "Teacher email registered successfully"
        else:
            return False, "Invalid email domain"

    def get_student_emails(self):
        """Get all registered student emails"""
        return self.student_manager.get_emails()

    def get_teacher_emails(self):
        """Get all registered teacher emails"""
        return self.teacher_manager.get_emails()