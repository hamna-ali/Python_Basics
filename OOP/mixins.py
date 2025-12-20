# class Admin:
#     def send_email(self):
#         return "Admin sending email"

# class Editor:
#     def send_email(self):
#         return "Editor sending email"

# class Subscriber:
#     def send_email(self):
#         return "Subscriber sending email"


# Define shared behaviors as mixins
class EmailMixin:
    def send_email(self, message):
        return f"{self.__class__.__name__} sending email: {message}"

class ReportMixin:
    def generate_report(self):
        return f"{self.__class__.__name__} generating report"

# User classes inherit only the behaviors they need
class Admin(EmailMixin, ReportMixin):
    pass

class Editor(EmailMixin):
    pass

class Subscriber:
    pass  # no special behavior

# Usage
admin = Admin()
editor = Editor()
subscriber = Subscriber()

print(admin.send_email("Welcome!"))
print(admin.generate_report())
print(editor.send_email("Hi Editor!"))

