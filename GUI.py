import Fertilization as fert
import tkinter as tk
from tkinter import Button, Entry, Label, Text, ttk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Fertilization calculator")
window.geometry("550x200")
icon = ImageTk.PhotoImage(Image.open("icone.png"))
window.iconphoto(True,icon)

### Creating Functions ###
def get_crop():
    crop = crops_list.get()

    if crop == "Milho":
        corn = fert.Corn(get_yield())
        return corn

    elif crop == "Soja":
        soybean = fert.Soybean(get_yield())
        return soybean
    else:
        wheat = fert.Wheat(get_yield())
        return wheat

def get_yield():
    yld = entry_yld.get()
    try:
       return float(yld)

    except ValueError:
        print("Error: Input is not a number")
    return None

def get_plotid():
    plot_id = entry_plot_id.get()
    soil = fert.Soil(plot_id)
    return soil



def calculator():
    soil = get_plotid()
    crop = get_crop()
    calculator = fert.FertCalc()
    correction = calculator.correction_fertilization(soil)
    maintenance = calculator.maintenance_fertilization(crop)
    fertilization = calculator.total_fertilization(correction,maintenance)
    lime = calculator.lime_required(crop,soil)
    output_N.delete("1.0", tk.END)
    output_P.delete("1.0", tk.END)
    output_K.delete("1.0", tk.END)
    output_Lime.delete("1.0",tk.END)
    output_N.insert(tk.END, fertilization['N'])
    output_P.insert(tk.END, fertilization['P'])
    output_K.insert(tk.END, fertilization['K'])
    output_Lime.insert(tk.END,lime)
    return fertilization


### CROP LIST ###
crops_list_label = Label(window,
                         text = "Selecione a Cultura:")
crops_list = ttk.Combobox(
    values = ["Soja","Milho","Trigo"],
    state = "readonly")
crops_list_label.place(x = 0,
                       y = 0) 
crops_list.place(x = 0,
                 y = 20)

### Plot ID ###
entry_plot_id_label = Label(window,
                            text = "Insira o talhão:")
entry_plot_id = Entry()
entry_plot_id_label.place(x = 0,
                          y = 50)
entry_plot_id.place(x = 0,
                    y = 70)

### Yield ###
entry_yld_label = Label(window,
                  text = "Insira a produtividade da cultura:")
entry_yld = Entry(width = 28)
entry_yld_label.place(x = 0,
                      y = 100)
entry_yld.place(x = 0,
                y = 120)
### Buttons ###
calculate_button = Button(window,
                          text = "Calcular",
                          font = ("Arial", 14),
                          command =calculator,
                          height = 2,
                          width = 10)
calculate_button.place(x = 280,
                       y = 60)

### Outputs Labels ###
output_N_label = Label(window,
                       text = "N (Kg/ha)")
output_P_label = Label(window,
                       text = "P205 (Kg/ha)")
output_K_label = Label(window,
                       text = "K2O (Kg/ha)")
output_Lime_label = Label(window,
                          text = "Calcário (T/ha)")

output_N_label.place(x = 0,
                     y = 150)
output_P_label.place(x = 150,
                     y = 150)
output_K_label.place(x = 300,
                     y = 150)
output_Lime_label.place(x = 450,
                        y = 150)



### Outputs ###
output_N = Text(window,
                height = 1,
                width = 12)
output_N.place(x = 0,
               y = 170)


output_P = Text(window,
                height = 1,
                width = 12)
output_P.place(x = 150,
               y = 170)


output_K = Text(window,
                height = 1,
                width = 12)
output_K.place(x = 300,
               y = 170)

output_Lime = Text(window,
                height = 1,
                width = 12)
output_Lime.place(x = 450,
                  y = 170)






window.mainloop()
