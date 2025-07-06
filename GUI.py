from tkinter import *
from tkinter.ttk import Combobox
from Fertilization import *



### Creating Main Window ###
window = Tk()



### Creating Functions ###
def get_crop():
    crop = crops_list.get()

    if crop == "Milho":
        corn = Corn(get_yield())  
        return corn

    elif crop == "Soja":
        soybean = Soybean(get_yield())
        return soybean
    else:
        wheat = Wheat(get_yield())
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
    soil = Soil(plot_id)
    return soil



def calculator():
    soil = get_plotid()
    crop = get_crop()
    calculator = FertCalc()
    correction = calculator.correction_fertilization(soil)
    maintenance = calculator.maintenance_fertilization(crop)
    fertilization = calculator.total_fertilization(correction,maintenance)
    output.delete("1.0",END)
    output.insert(END,fertilization)
    return fertilization



### Crop ###
crops = ["Milho","Soja","Trigo"]
crops_list = Combobox(window,
                      values = crops)
crops_list.set("Escolha a cultura de interesse.")
crops_list.pack(side = "left")



### Plot ID ###
label_plot_id = Label(window,text = "Plot ID:")
label_plot_id.pack(side = "left")
entry_plot_id = Entry(window)
entry_plot_id.pack(side = "left")



### Yield ###
label_yld = Label(window,text = "Yield:")
label_yld.pack(side = "left")
entry_yld = Entry(window)
entry_yld.pack(side = "left")



### Calculate ###
calculate_button = Button(window,
                          text = "Calculate",
                          command = calculator)
calculate_button.pack()
output = Text(window,
              height = 5,
              width = 30)
output.pack(side = "right")

### Main Loop ###
window.mainloop()
