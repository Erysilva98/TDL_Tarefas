import PySimpleGUI as sg

layout = [
    [sg.Button('xMark'),sg.Text('TAREFA'),sg.Input(''),sg.Button('EDITAR'),sg.Button('REMOVER')],
    [sg.Button('NOVA TAREFA')]
]

janela = sg.Window('TO DO LIST',layout)

envent,value = janela.read()