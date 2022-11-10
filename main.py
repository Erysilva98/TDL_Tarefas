import PySimpleGUI as sg

layout = [
    [sg.Text('TAREFA'),sg.Input(''),sg.Button('REMOVER')],
    [sg.Button('NOVA TAREFA')]
]

janela = sg.Window('TO DO LIST',layout)

envent,value = janela.read()