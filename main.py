import PySimpleGUI as sg

layout = [
    [sg.CalendarButton("Informe Data", size=(10,1)),sg.T("-- -- -- --",key="-DATA-")],
    [sg.T("Nova Tarefa:",size=(10,1)),sg.I(key="-TASK-",font=("None 15"),size=(32,1))],
    [sg.Table(values='',headings=["Indice","Data","Tarefa"],key="-TABLE-",size=(500,10),auto_size_columns=False,col_widths=[5,9,30],vertical_scroll_only=False,justification='1',font="None 15")],
    [sg.B("Add",size=(10,1),button_color="green"),sg.B("Del",key="-DEL-",size=(10,1),button_color="red"),sg.Exit("Sair",size=(10,1))],

]

janela = sg.Window("TDL GERENCIE SUAS TAREFAS",layout)
lTarefas = []
contador = 1

while True:
    evento, valor = janela.read()
    if evento in ("Sair",sg.WIN_CLOSED):
        janela.close()
        break

    elif evento == "Add":
        data = janela["-DATA-"].get().split()[0]
        tarefa = [[contador,data,valor["-TASK-"]]]
        lTarefas += tarefa 
        janela["-TABLE-"].update(lTarefas)
        janela["-TASK-"].update('')
        contador += 1

    print(evento,valor)