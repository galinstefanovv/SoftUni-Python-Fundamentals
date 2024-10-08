data = input()
companies = {}

while data != "End":
    company, emp = data.split(" -> ")
    if company not in companies.keys():
        companies[company] = []
    if emp not in companies[company]:
        companies[company].append(emp)
    data = input()

for company_name, employee_id in companies.items():
    print(f"{company_name}")
    for name in employee_id:
        print(f"-- {name}")