import PySimpleGUI as sg
layout=[
    [sg.Text("ENTER THE TEXT"),sg.InputText("",key='name')],[sg.Button("Add"),sg.Button("exit")]]
window=sg.Window('GUI',layout)
l=[]
while True:
    Button, values = window.Read()
    if Button =='Add':
        l.append(values['name'])
        window.FindElement('name').update("")
    elif Button=='exit':
        sg.popup("names are",l)
        break
