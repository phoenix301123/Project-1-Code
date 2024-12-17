#PYTHON 
#PYTHON 
def process_commands():
    database = set()

    while True:
        key = input().strip()
        if key == "*":
            break
        database.add(key)

    while True:
        command = input().strip()
        if command == "***":
            break
        
        cmd, value = command.split()
        
        if cmd == "find":
            if value in database:
                print(1)
            else:
                print(0)
        elif cmd == "insert":
            if value in database:
                print(0)
            else:
                database.add(value)
                print(1)

process_commands()
