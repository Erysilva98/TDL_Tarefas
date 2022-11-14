import PySimpleGUI as sg

layout = [
    [sg.CalendarButton("Set Date", size=(10,1)),sg.T("-- -- -- --",key="-DATA-")],
    [sg.T("Write Task:",size=(10,1)),sg.I(key="-TASK-",font=("None 15"),size=(32,1))],
    [sg.Table(values='',headings=["Index","Date","Task"],key="-TABLE-",size=(500,10),auto_size_columns=False,col_widths=[5,9,30],vertical_scroll_only=False,justification='1',font="None 15")],
    [sg.B("Add",size=(10,1),button_color="green"),sg.B("Delete",key="-DEL-",size=(10,1),button_color="red"),sg.Exit(size=(10,1))],

]

window = sg.Window("TDL GERENCIE SUAS TAREFAS",layout)
tasks = []
counter = 1

while True:
    event, values = window.read()
    if event in ("Exit",sg.WIN_CLOSED):
        window.close()
        break

    elif event == "Add":
        date = window["-DATA-"].get().split()[0]
        task = [[counter,date,values["-TASK-"]]]
        tasks += task 
        window["-TABLE-"].update(tasks)
        window["-TASK-"].update('')
        counter += 1

    print(event,values)