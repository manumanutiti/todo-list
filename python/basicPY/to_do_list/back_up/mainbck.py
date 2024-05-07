while True:
    # get user input and strip space chars from it
    user_action = input("add, show, edit, completed, clear or exit: ")
    user_action = user_action.strip()

    
    if 'add' in user_action:
        todo = user_action[4:] + "\n"
        with open('python\\basicPY\\to_do_list\\todos.txt', 'r') as file:
            todos = file.readlines()
                

        with open('python\\basicPY\\to_do_list\\todos.txt', 'w') as file:
            todos.append(todo)
            file.writelines(todos)
                
    
            
    elif 'show' in user_action:
        with open('python\\basicPY\\to_do_list\\todos.txt', 'r') as file:
            content = file.readlines()
                
                
            for index, item in enumerate(content):
                row = f"{index + 1}- {item.strip()}"
                print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1
        with open('python\\basicPY\\to_do_list\\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number)
        new_todo = input("new todo: ") + "\n"
        todos.append(new_todo)
            
        with open('python\\basicPY\\to_do_list\\todos.txt', 'w') as file:
                file.writelines(todos)
            

    elif "complete" in user_action:
        number = int(user_action[9:])
        number -= 1
        with open('python\\basicPY\\to_do_list\\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number)
            
        with open('python\\basicPY\\to_do_list\\todos.txt', 'w') as file:
            file.writelines(todos)

    elif  'exit' in user_action:
        print("[!] Saliendo...\n")
        break

    elif 'clear' in user_action:

        with open('python\\basicPY\\to_do_list\\todos.txt', 'w') as file:
            file.write("")
        print("Empty list...")
    else:
         print("NO VALID")
    