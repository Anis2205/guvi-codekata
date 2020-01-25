import PySimpleGUI as sg
layout=[[sg.InputCombo(['coice1','choice2'])],[sg.Listbox(values=['List1','List2'],size=(30,6))],[sg.Button("ok")]]

window=sg.Window('GUI',layout)
button,values=window.Read()
sg.popup("GUI",button,values)
