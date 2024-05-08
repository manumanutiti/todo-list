def get_todos(filepath="python\\basicPY\\to_do_list\\todos.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()

    return todos

def write_todos(todos_arg, filepath="python\\basicPY\\to_do_list\\todos.txt"):
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

def clear_todos(filepath):
    with open(filepath, 'w') as file:
        file.write("")
        print("List emptied...")
