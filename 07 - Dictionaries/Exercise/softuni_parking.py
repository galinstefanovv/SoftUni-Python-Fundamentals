n = int(input())
cars = {}
for i in range(1, n+1):
    command = input().split()
    cmd = command[0]
    key = command[1]
    if cmd == "register":
        value = command[2]
        if key not in cars.keys():
            cars[key] = value
            print(f"{key} registered {value} successfully")
        else:
            print(f"ERROR: already registered with plate number {cars[key]}")
    elif cmd == "unregister":
        if key not in cars.keys():
            print(f"ERROR: user {key} not found")
        else:
            del cars[key]
            print(f"{key} unregistered successfully")
for username, plate in cars.items():
    print(f"{username} => {plate}")