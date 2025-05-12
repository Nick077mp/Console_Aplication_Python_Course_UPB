class EmailDisplay:
    def __init__(self, email_register):
        self.email_register = email_register

    def display_emails(self, email_type="all"):
        """Display emails based on type (all, student, or teacher)"""
        if email_type in ["all", "student"]:
            student_emails = self.email_register.get_student_emails()
            print("\nStudent Emails:")
            for id_, email in student_emails.items():
                print(f"{id_}. {email}")

        if email_type in ["all", "teacher"]:
            teacher_emails = self.email_register.get_teacher_emails()
            print("\nTeacher Emails:")
            for id_, email in teacher_emails.items():
                print(f"{id_}. {email}")
                print(f'{dict(teacher_emails.items())}')