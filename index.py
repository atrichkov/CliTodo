import json
from prettytable import PrettyTable

print('========================= Command TODO line tool =========================');

commands = {
    '1': 'Add new todo',
    '2': 'List all todos',
}

# List possible commands
for x in commands:
    print(x + ' - ' + commands[x])

def loadFileData():
    with open('todos.json', 'r') as file:
        data = file.read()
        return json.loads(data)

def addNewTodo():
    try:
        data = loadFileData()
    except FileNotFoundError:
        data = [];

    todoName = str(input('Enter new todo name: '))
    todoDesc = str(input('Enter new todo description (enter to skip): '))
    # Save data from input
    file = open('todos.json', 'w+')
    data.append({"name": todoName, "desc": todoDesc})
    file.write(json.dumps(data))

def listTodos():
    table = PrettyTable()
    table.field_names = ['Name', 'Description']
    todosList = loadFileData()
    for todo in todosList:
        table.add_row([todo["name"], todo["desc"]])
    
    print(table)

inpCommand = int(input('Select option from above: '))

if inpCommand == 1:
    addNewTodo()
elif inpCommand == 2:
    listTodos()