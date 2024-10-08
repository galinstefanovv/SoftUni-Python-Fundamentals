def data_types(string, type):
    if string == "int":
        data = int(type) * 2
        print(data)
    elif string == "real":
        data = float(type) * 1.5
        print(f'{data:.2f}')
    elif string == "string":
        print(f'${type}$')


input_string = input()
input_type = input()
data_types(input_string, input_type)