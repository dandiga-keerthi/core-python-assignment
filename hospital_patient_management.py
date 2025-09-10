def search_patients(patients, disease):
    return [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
n = int(input("Enter number of patients: "))
patients = []
for _ in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter patient disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
search_disease = input("Enter disease to search: ")
result = search_patients(patients, search_disease)
formatted_result = "[" + ", ".join(f'"{name}"' for name in result) + "]"
print(f'Patients with {search_disease}: {formatted_result}')
