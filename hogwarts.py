"""
# Using a list:
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print (i, students[i])
"""
"""
# Using a dictionary:
students = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin",
            }

for student in students:
    print (student, students[student], sep = " - ")
"""

# Using a list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},    
]
for student in students:
    print (student["name"], student["house"], student["patronus"], sep = ", ")