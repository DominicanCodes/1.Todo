FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """Return a list of todos in a text document"""
    with open(filepath, 'r') as file:
            todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the list of todos in a text document"""
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

if __name__ == "__main__": #Dont show when imported
    print('functions run directly')