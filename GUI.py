from tkinter import *

counter = 0
def click():
    global counter
    counter+= 1
    print(counter)


window = Tk() #Cria uma instância de uma janela
window.geometry("800x600")
window.title("Fertilization Calculator")

icon = PhotoImage(file="icone.png")
window.iconphoto(True, icon)
window.configure(background = "#5fb646")

#Label
label = Label(window,
              text="Fertilization Calculator",
              font = ("arial",40,"bold"),
              fg = "white",
              bg = "black",
              relief = "groove",#Borda 
              bd = 5) #Borda espessura
label.pack()


button = Button(window,
                text = "Calculate",
                command=click)
button.pack()


window.mainloop()
