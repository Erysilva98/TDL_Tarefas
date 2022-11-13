import PySimpleGUI as sg

layout = [
    [sg.CalendarButton("Data", size=(10,1)),sg.T("-- -- -- --", key="-DIA-")],
    [sg.T("Escreva:",size=(10,1)),sg.I(key="-TAR-",font=("None 15"),size=(32,1))],
    [sg.Table(values='', headings=["INDICE","DATA","TAREFA"],key="-TABELA-",size=(500,10),auto_size_columns=False,col_widths=[7,9,30],vertical_scroll_only=False,justification='left',font="None 15")],
    [sg.B("ADICIONAR",size=(10,1),button_color="green"),sg.B("REMOVER",key="-DEL-",button_color="red"),sg.Exit("FECHAR",size=(10,1))],
]

#,sg.B("REMOVER",key="-DEL-"),sg.EXIT()

janela = sg.Window('TDL - GERENCIE SUAS TAREFAS',layout)
tarefa = []
contador = 1

while True:
    evento, valor = janela.read()

    if evento in ("FECHAR",sg.WIN_CLOSED):
        janela.close()
        break

    elif evento == "ADICIONAR":
        data = janela["-DIA-"].get().split()[0]
        tarefa = [[contador,data,valor["-TAR-"]]]
        tarefa += tarefa
        janela["-TABELA-"].update(tarefa)
        janela["-TAR-"].update('')
        contador += 1

    print(evento,valor)