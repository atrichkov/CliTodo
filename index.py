import json
from prettytable import PrettyTable

print('========================= Command TODO line tool =========================');

commands = {
    '1': 'Add new todo',
    '2': 'List all todos',
    '3': 'Delete todo',
}

# List possible commands
for x in commands:
    print(x + ' - ' + commands[x])

def loadFileData():
    with open('todos.json', 'r') as file:
        data = file.read()
        return json.loads(data)

def saveData(data):
    file = open('todos.json', 'w+')
    file.write(json.dumps(data))

def addNewTodo():
    try:
        data = loadFileData()
    except FileNotFoundError:
        data = [];

    todoName = str(input('Enter new todo name: '))
    todoDesc = str(input('Enter new todo description (enter to skip): '))
    # Save data from input
    data.append({"name": todoName, "desc": todoDesc})
    saveData(data)

def listTodos():
    table = PrettyTable()
    table.field_names = ['#', 'Name', 'Description']
    todosList = loadFileData()

    index = 1
    for todo in todosList:
        table.add_row([index, todo["name"], todo["desc"]])
        index += 1
    
    print(table)

inpCommand = int(input('Select option from above: '))

if inpCommand == 1:
    addNewTodo()
elif inpCommand == 2:
    listTodos()
elif inpCommand == 3:
    indexTodo = int(input('Select todo number that you want to delete ? '))
    data = loadFileData()

    if len(data) < indexTodo:
        print("Sorry, selected todo don't exist")

    counter = 1
    for x in data:
        if (counter == indexTodo):
            del data[counter-1]
        counter += 1
    saveData(data)