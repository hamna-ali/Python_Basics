def student_info(*args, **kwargs):
    print("Positional Arguments (args):", args)
    print("Keyword Arguments (kwargs):", kwargs)

student_info("Hamna", 22, city="Lahore", country="Pakistan")


courses = ["Math", "Science", "History"]
info = {"name": "Ali", "age": 20, "city": "Karachi", "country": "Pakistan"}

student_info(*courses, **info)