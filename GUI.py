import Fertilization as fert
import tkinter as tk
from tkinter import Button, Entry, Label, Text, ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Fertilization calculator")
root.geometry("550x200")
icon = ImageTk.PhotoImage(Image.open("icone.png"))
root.iconphoto(True, icon)

frame_menu = tk.Frame(root)
frame_calculadora = tk.Frame(root)
frame_inserir_dados = tk.Frame(root)

frames = {}
frames["Menu"] = frame_menu
frames["Calculadora"] = frame_calculadora
frames["Inserir Dados"] = frame_inserir_dados

### Funções ###
def select_frame(frame):
    for f in frames.values():
        f.pack_forget()
    frames[frame].pack(fill="both", expand=True)


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
    fertilization = calculator.total_fertilization(correction, maintenance)
    lime = calculator.lime_required(crop, soil)
    output_N.delete("1.0", tk.END)
    output_P.delete("1.0", tk.END)
    output_K.delete("1.0", tk.END)
    output_Lime.delete("1.0", tk.END)
    output_N.insert(tk.END, fertilization['N'])
    output_P.insert(tk.END, fertilization['P'])
    output_K.insert(tk.END, fertilization['K'])
    output_Lime.insert(tk.END, lime)
    return fertilization

### Menu Principal ###
Label(frame_menu, text = "Menu Principal").pack()
Button(frame_menu,text = "Calculadora",command = lambda: select_frame("Calculadora")).pack()
Button(frame_menu,text = "Inserir Dados de Solo",command = lambda: select_frame("Inserir Dados")).pack()

### Menu Calculadora ###
crops_list_label = Label(frame_calculadora,
                         text="Selecione a Cultura:")
crops_list_label.pack(anchor="w", padx=5, pady=(0,2))

crops_list = ttk.Combobox(frame_calculadora,
                          values=["Soja","Milho","Trigo"],
                          state="readonly",
                          width=15)
crops_list.pack(anchor="w", padx=5, pady=(0,8))

entry_plot_id_label = Label(frame_calculadora,
                            text="Insira o talhão:")
entry_plot_id_label.pack(anchor="w", padx=5, pady=(0,2))

entry_plot_id = Entry(frame_calculadora, width=20)
entry_plot_id.pack(anchor="w", padx=5, pady=(0,8))

entry_yld_label = Label(frame_calculadora,
                        text="Insira a produtividade da cultura:")
entry_yld_label.pack(anchor="w", padx=5, pady=(0,2))

entry_yld = Entry(frame_calculadora, width=28)
entry_yld.pack(anchor="w", padx=5, pady=(0,8))

calculate_button = Button(frame_calculadora,
                          text="Calcular",
                          font=("Arial", 14),
                          command=calculator,
                          height=2,
                          width=10)
calculate_button.pack(anchor="e", padx=10, pady=(0,15))

output_N_label = Label(frame_calculadora,
                       text="N (Kg/ha)")
output_N_label.pack(anchor="w", padx=5, pady=(0,2))

output_P_label = Label(frame_calculadora,
                       text="P205 (Kg/ha)")
output_P_label.pack(anchor="w", padx=155, pady=(0,2))

output_K_label = Label(frame_calculadora,
                       text="K2O (Kg/ha)")
output_K_label.pack(anchor="w", padx=300, pady=(0,2))

output_Lime_label = Label(frame_calculadora,
                          text="Calcário (T/ha)")
output_Lime_label.pack(anchor="w", padx=450, pady=(0,2))

output_N = Text(frame_calculadora,
                height=1,
                width=12)
output_N.pack(anchor="w", padx=5, pady=(0,8))

output_P = Text(frame_calculadora,
                height=1,
                width=12)
output_P.pack(anchor="w", padx=155, pady=(0,8))

output_K = Text(frame_calculadora,
                height=1,
                width=12)
output_K.pack(anchor="w", padx=300, pady=(0,8))

output_Lime = Text(frame_calculadora,
                   height=1,
                   width=12)
output_Lime.pack(anchor="w", padx=450, pady=(0,8))



select_frame("Menu")
root.mainloop()

