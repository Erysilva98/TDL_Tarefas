import PySimpleGUI as sg

layout = [
    [sg.Checkbox(''),sg.CalendarButton('Data',key='-DATA-'),sg.Text('TAREFA'),sg.Input(''),sg.Button('EDITAR'),sg.Button('REMOVER')],
    [sg.Button('NOVA TAREFA')]
]

janela = sg.Window('TDL - GERÊNCIE SUAS TAREFAS',layout)


while True:
    envent,value = janela.read()

    if envent in ('Exit',sg.WIN_CLOSED):
        janela.close()
        break

    print(envent,value)