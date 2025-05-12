class Student:
    def __init__(self):
        self.emails = {}
        self.counter = 1

    def add_email(self, email):
        """Add a student email to the dictionary"""
        self.emails[self.counter] = email
        self.counter += 1

    def get_emails(self):
        """Return all student emails"""
        return self.emails

    def search_email(self, search_term):
        """Search for an email that contains the search term"""
        return {k: v for k, v in self.emails.items() if search_term.lower() in v.lower()}