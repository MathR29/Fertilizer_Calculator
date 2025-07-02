from tkinter import *

##Functions##
counter = 0
def click():
    global counter
    counter+= 1
    print(counter)

def submit():
    name = entry.get()
    print(f'Your name is {name}')
#############

window = Tk() #Cria uma instância de uma janela
window.geometry("800x600")
window.title("Fertilization Calculator")

icon = PhotoImage(file="icone.png")
window.iconphoto(True, icon)
window.configure(background = "#5fb646")

##Label###
label = Label(window,
              text="Fertilization Calculator",
              font = ("arial",40,"bold"),
              fg = "white",
              bg = "black",
              relief = "groove",#Borda 
              bd = 5) #Borda espessura
label.pack()
#########

##Button##
button = Button(window,
                text = "Calculate",
                command=click)
button.pack()
#######


##Entry##
entry = Entry(window,

              font = ("arial",20))
entry.insert(0,"What is your name?")
entry.pack(side = "left")

submit = Button(window,
                text = "Submit",
                command = submit)
submit.pack(side =  "right")
#########



window.mainloop()
