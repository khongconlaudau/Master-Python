    # String is immutable

course = "   python programming  "
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())     # right strip removes white space at the end
print(course.lstrip())     # left strip removes white space at the beginning
        # Python is Case Sensitive Language
print(course.find("pro"))
print("pro" in course)
print("swift" not in course)
