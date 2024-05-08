FILEPATH = "todo-list\\todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()

    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

def clear_todos(filepath):
    with open(filepath, 'w') as file:
        file.write("")
        print("List emptied...")
