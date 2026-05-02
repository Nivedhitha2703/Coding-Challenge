students = []

# Number of students
n = int(input())

# Input data
for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Get unique sorted grades
grades = sorted(set([s[1] for s in students]))

# Second lowest grade
second_lowest = grades[1]

# Get names with second lowest grade
names = [s[0] for s in students if s[1] == second_lowest]

# Sort names alphabetically
names.sort()

# Print results
for name in names:
    print(name)
