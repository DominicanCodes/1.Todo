# from functions import *
import modules.functions as functions # /To Use: functions.method()/
import time

print("\nTodays date: "+ time.strftime('%b %d, %Y %H:%M:%S'))
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # match user_action:
    #         case 'add':
    if user_action.lower().startswith('add'):
        if user_action[4:] == '':
            print("Todo item entered was invalid.")
            continue

        todo = user_action[4:]

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = functions.get_todos()

        todos.append(todo + '\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()
        functions.write_todos(todos)

    elif user_action.lower().startswith('show'):
        todos = functions.get_todos()

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            # item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.lower().startswith('edit'):
        try:
            number = int(user_action[5:]) - 1 # int(input("Number of the todo to edit: ")) - 1

            todos = functions.get_todos()

            new_todo = input("Enter todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.lower().startswith('complete'):
        try:
            number = int(user_action[9:]) - 1 #int(input("Number of the todo to complete: ")) - 1
            
            todos = functions.get_todos()
            
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Please enter a todo number to complete.")
            continue

    elif user_action.lower().startswith('exit'):
        break
    else:
        print('This command is invalid.')
    
    print('\n')

print('Bye\n')
