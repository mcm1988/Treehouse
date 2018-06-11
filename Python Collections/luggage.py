def packer(name=None, **kwargs):
    print(kwargs)


def unpacker(dictionary):
        print("Hi {first_name} {last_name}!".format(**dictionary))


packer(name="Sean", num=42, spanish_inquisition=None)
unpacker({"last_name": "Steberis", "first_name": "Sean"})

course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 198, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long". format(course, minutes))
