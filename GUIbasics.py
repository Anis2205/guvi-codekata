import PySimpleGUI as sg
layout=[
    [sg.Text("ENTER THE TEXT"),sg.InputText("",key='name')],[sg.Button("ok")]]
window=sg.Window('GUI',layout)
button,values=window.Read()
sg.popup("GUI",button,values)
