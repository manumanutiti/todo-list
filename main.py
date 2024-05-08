from functions import get_todos, write_todos, clear_todos
import time

now = time.strftime("%b %d, %Y %H:%M")
print(now)


while True:
    # get user input and strip space chars from it
    user_action = input("add, show, edit, complete, clear or exit: ")
    user_action = user_action.strip()

    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        
        todos = get_todos()
        todos.append(todo)
                
        write_todos(filepath="python\\basicPY\\to_do_list\\todos.txt", todos_arg=todos)
                
    
            
    elif user_action.startswith("show"):
        
        todos = get_todos()                
                
        for index, item in enumerate(todos):
            row = f"{index + 1}- {item.strip()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            todos = get_todos()

            todos.pop(number)
            new_todo = input("new todo: ") + "\n"
            todos.append(new_todo)
                
            write_todos(filepath="python\\basicPY\\to_do_list\\todos.txt", todos_arg=todos)

        except ValueError:
            print("Your command is not valid")
            continue
                

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number -= 1
            todos = get_todos()

            todos.pop(number)
                
            write_todos(filepath="python\\basicPY\\to_do_list\\todos.txt", todos_arg=todos)

        except IndexError:
            print("theres no index with that number")
            continue

    elif user_action.startswith('exit'):
        print("[!] Saliendo...\n")
        break

    elif user_action.startswith('clear'):

        clear_todos("python\\basicPY\\to_do_list\\todos.txt")
    else:
         print("NO VALID")
    
    