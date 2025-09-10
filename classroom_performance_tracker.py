def calculate_averages(students):
    return {name: round(sum(marks) / len(marks), 2) for name, marks in students.items()}
def find_top_performer(averages):
    return max(averages, key=averages.get)

students = {}
n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("\nEnter student name: ")
    marks = list(map(int, input(f"Enter marks for {name} (comma separated): ").split(",")))
    students[name] = marks

averages = calculate_averages(students)
top_performer = find_top_performer(averages)

print("\nAverage Marks:", averages)
print(f'Top Performer: "{top_performer}"')
