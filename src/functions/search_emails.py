class EmailSearch:
    def __init__(self, email_register):
        self.email_register = email_register

    def search_emails(self, search_term):
        """Search for emails containing the search term"""
        student_results = self.email_register.student_manager.search_email(search_term)
        teacher_results = self.email_register.teacher_manager.search_email(search_term)

        results = {
            "students": student_results,
            "teachers": teacher_results
        }
        return results