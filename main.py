import PySimpleGUI as sg

global pos
global contador

lTarefas = []
contador = 1
pos = 0

layout = [
    [sg.CalendarButton("ENTREGAR ", size=(10,1)),sg.T("-- -- -- --",key="-DATE-")],
    [sg.T("NOME ",size=(10,1)),sg.I(key="-USER-",font=("None 15"),size=(15,1))],
    [sg.T("PROJETO ",size=(10,1)),sg.I(key="-PROJ-",font=("None 15"),size=(15,1))],
    [sg.T("TAREFA ",size=(10,1)),sg.I(key="-TASK-",font=("None 15"),size=(35,1))],
    [sg.Table(values='',headings=["N°","PRIORIDADE","USUÁRIO","PROJETO","TAREFA"],key="-TABLE-",enable_events=True,size=(500,10),auto_size_columns=False,col_widths=[4,10,15,15,35],vertical_scroll_only=False,justification='1',font="None 15")],
    [sg.B("ADICIONAR",key="-ADD-",size=(10,1),button_color="green"),sg.B("EDITAR",key="-EDT-",size=(10,1),button_color="black"),sg.B("SALVAR",key="-SAVE-",size=(10,1),button_color="green"),sg.B("ORDENAR",key="-ORD-",size=(10,1),button_color="black"),sg.B("DELETAR",key="-DEL-",size=(10,1),button_color="red"),sg.Exit("SAIR",key="-ESC-",size=(10,1))],
]

janela = sg.Window("TDL AGENDA DE TAREFAS",layout)

def ordenar(lTarefas):
    troca = True
    tam = len(lTarefas)-1

    while tam > 0 and troca:
        troca = False
        for i in range(tam):
            if lTarefas[i][1]>lTarefas[i+1][1]:
                troca = True
                temp = lTarefas[i][1]
                lTarefas[i][1] = lTarefas[i+1][1]
                lTarefas[i+1][1] = temp
        tam = tam-1

    return lTarefas

def add(valor, lTarefas, contador):
    data = janela["-DATE-"].get().split()[0]
    tarefa = [[contador,data,valor["-USER-"],valor["-PROJ-"],valor["-TASK-"]]]
    lTarefas += tarefa 
    janela["-TABLE-"].update(lTarefas)
    janela["-USER-"].update('')
    janela["-PROJ-"].update('')
    janela["-TASK-"].update('') 

    return lTarefas, contador

def edt(valor,lTarefas):
    if valor["-TABLE-"]:
        indice = valor["-TABLE-"][0]
        nUser = lTarefas[indice][2]
        nSetr = lTarefas[indice][3]
        nTask = lTarefas[indice][4]
        janela["-USER-"].update(nUser)
        janela["-PROJ-"].update(nSetr)
        janela["-TASK-"].update(nTask)  
        del lTarefas[indice]  
    else:
        pass

    return lTarefas

def save(valor,lTarefas,pos):
    data = janela["-DATE-"].get().split()[0]
    tarefa = [[pos,data,valor["-USER-"],valor["-PROJ-"],valor["-TASK-"]]]
    lTarefas += tarefa 
    janela["-TABLE-"].update(lTarefas)
    janela["-TASK-"].update('')
    janela["-PROJ-"].update('')
    janela["-USER-"].update('')

    return lTarefas   

def deleta(valor,lTarefas):
    if valor["-TABLE-"]:
        indice = valor["-TABLE-"][0]
        del lTarefas[indice]
        janela["-TABLE-"].update(lTarefas)
    else:
        pass

    return lTarefas

while True:
    evento, valor = janela.read()
    if evento in ("-ESC-",sg.WIN_CLOSED):
        janela.close()
        break

    elif evento == "-ADD-":
        add(valor,lTarefas,contador)
        contador += 1

    elif evento == "-EDT-":
        if valor["-TABLE-"]:
            indice = valor["-TABLE-"][0]
            edIndice = lTarefas[indice][0]
            pos = edIndice
            edt(valor,lTarefas)
        else:
            pass

    elif evento == "-SAVE-":
        save(valor,lTarefas,pos)

    elif evento == "-ORD-": 
        ordenar(lTarefas)
        janela["-TABLE-"].update(lTarefas)

    elif evento == "-DEL-":
        if valor["-TABLE-"]:
            deleta(valor,lTarefas)
        else:
            pass
    
    else:
        pass
            

    