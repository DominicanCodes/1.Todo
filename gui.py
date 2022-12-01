from modules import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Dark Amber")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter to-do", key='todo')
add_button = sg.Button(image_subsample=8, 
                        image_source="icons/plus.png",
                        mouseover_colors="LightGrey",
                        tooltip='Add to-do', key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                    enable_events=True, size=[45, 10])
edit_button = sg.Button(image_subsample=4, 
                        image_source="icons/edit.png",
                        mouseover_colors="LightGrey",
                        tooltip='Edit to-do', key="Edit")
complete_button = sg.Button(image_subsample=4, 
                        image_source="icons/check-mark.png",
                        mouseover_colors="LightGrey",
                        tooltip='Complete to-do', key="Complete")
exit_button = sg.Button("Exit")

column_container = sg.Column(layout=[[edit_button], [complete_button]])

window = sg.Window('My To-Do App', 
                    layout=[[clock],
                            [label], 
                            [input_box, add_button],
                            [list_box, column_container],
                            [exit_button]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
        
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            
            if new_todo == '\n':
                sg.popup("Please enter an item first.", font=("Helvetica", 20))
                continue
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        case "Exit":
            break

        case "__TIMEOUT__":
            continue

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

    print(1, event)
    print(2, values)
    print(3, values['todos'])

window.close()


# For Windows Packet: set-executionpolicy remotesigned -scope currentuser
# pip install pyinstaller
# pyinstaller --onefile --windowed --clean gui.py

""" 
If you dont use the --onefile command, 
you can just drag and drop the images into the folder your exe is in.
Or drop in the folder of images.

If you do use onefile, you need to modify the .spec file you get 
when you run the code pyinstaller script.py. Then 
run pyinstaller scriptname.spec. 

edit the datas variable somewhat like this

datas = [('src/image.png', '.'),
         ('src/image1.png', '.')]

datas = [('icons/plus.png', '.'), ('icons/edit.png', '.'), ('icons/check-mark.png', '.'), ('icons/minus.png', '.')]
"""