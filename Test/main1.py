import PysimpleGUI as sg

layout = [
    [sg.CalendarButton("Informe Data", size=(10,1)),sg.T("-- -- -- --",key="-DATE-")],
    [sg.T("Ordem para:",size=(10,1)),sg.I(key="-USER-",font=("None 15"),size=(20,1))],
    [sg.T("Nova Tarefa:",size=(10,1)),sg.I(key="-TASK-",font=("None 15"),size=(32,1))],
    [sg.Table(values='',headings=["Indice","Data","Nome","Tarefa"],key="-TABLE-",enable_events=True,size=(500,10),auto_size_columns=False,col_widths=[5,9,20,30],vertical_scroll_only=False,justification='1',font="None 15")],
    [sg.B("SALVAR",key="-SAVE-",size=(10,1),button_color="green"),sg.B("EDITAR",key="-EDT-",size=(10,1),button_color="black"),sg.B("DELETAR",key="-DEL-",size=(10,1),button_color="red"),sg.Exit("SAIR",key="-ESC-",size=(10,1))],

]

janela = sg.Window("TDL GERENCIE SUAS TAREFAS",layout)
lTarefas = []
contador = 1

while True:
    evento, valor = janela.read()
    if evento in ("-ESC-",sg.WIN_CLOSED):
        janela.close()
        break

    elif evento == "-SAVE-":
        data = janela["-DATE-"].get().split()[0]
        tarefa = [[contador,data,valor["-USER-"],valor["-TASK-"]]]
        lTarefas += tarefa 
        janela["-TABLE-"].update(lTarefas)
        janela["-TASK-"].update('')
        janela["-USER-"].update('')
        contador += 1

    elif evento == "-EDT-":
        if valor["-TABLE-"]:
            indice = valor["-TABLE-"][0]
            nUser = lTarefas[indice][2]
            nTask = lTarefas[indice][3]
            janela["-USER-"].update(nUser)
            janela["-TASK-"].update(nTask)
            del lTarefas[indice]
        
    if evento == "-SAVE-":
        pass
                                      
    elif evento == "-DEL-":
        if valor["-TABLE-"]:
            indice = valor["-TABLE-"][0]
            del lTarefas[indice]
            janela["-TABLE-"].update(lTarefas)
            

    