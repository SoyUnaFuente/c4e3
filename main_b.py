students = ["Emmie Grey",
"Andre Hills",
"Gurpreet Atherton",
"Johan Stewart",
"Joseff Hurst",
"Margot Conrad",
"Matteo Whitaker",
"Mekhi Hussain",
"Sherry Macdonald",
"Mathew Cano",
"Cara O'Moore",
"Kush Gonzalez",
"Soren Clark",
"Inaayah Broadhurst",
"Ruth Lawrence",
"Nafisa Nairn",
"Zachariah Velasquez"]


students = [space.replace(" ", "_") for space in students]

for name in range(len(students)):
    students[name] = students[name].lower()

print(students)

