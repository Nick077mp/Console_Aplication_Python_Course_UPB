from functions.register_emails import EmailRegister
from functions.show_emails import EmailDisplay
from functions.search_emails import EmailSearch
from Users.student import Student

def display_menu():
    """Display the main menu options"""
    print("\n=== Email Management System ===")
    print("1. Register new email")
    print("2. View registered emails")
    print("3. Search for email")
    print("4. Exit")
    return input("Select an option (1-4): ")

def main():
    email_register = EmailRegister()
    email_display = EmailDisplay(email_register)
    email_search = EmailSearch(email_register)

    while True:
        option = display_menu()

        if option == "1":
            email = input("Enter email address: ")
            success, message = email_register.classify_and_register_email(email)
            print(message)

        elif option == "2":
            print("\nDisplay options:")
            print("1. All emails")
            print("2. Student emails only")
            print("3. Teacher emails only")
            display_option = input("Select display option (1-3): ")

            if display_option == "1":
                email_display.display_emails("all")
            elif display_option == "2":
                email_display.display_emails("student")
            elif display_option == "3":
                email_display.display_emails("teacher")
            else:
                print("Invalid option")

        elif option == "3":
            search_term = input("Enter search term: ")
            results = email_search.search_emails(search_term)
            
            if results["students"]:
                print("\nMatching Student Emails:")
                for id_, email in results["students"].items():
                    print(f"{id_}. {email}")
                    
            if results["teachers"]:
                print("\nMatching Teacher Emails:")
                for id_, email in results["teachers"].items():
                    print(f"{id_}. {email}")
                    
            if not results["students"] and not results["teachers"]:
                print("No matching emails found")

        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()