from tkinter import *
from tkinter.ttk import Combobox
from Fertilization import *



### Creating Main Window ###
window = Tk()



### Creating Functions ###
def get_crop():
    crop = crops_list.get()
    return print(crop)

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
    print(soil.deficits())
    return



### Crop ###
crops = ["Corn","Soybeans","Wheat"]
crops_list = Combobox(window,values = crops)
crops_list.set("Select a desired crop")
crops_list.pack(side = "left")



### Plot ID ###
label_plot_id = Label(window,text = "Plot ID:")
label_plot_id.pack(side = "left")
entry_plot_id = Entry(window)
entry_plot_id.pack(side = "left")

button_plot_id = Button(window,
                        text = "Submit Plot ID",
                        command = get_plotid)
button_plot_id.pack(side = "left")



### Yield ###
label_yld = Label(window,text = "Yield:")
label_yld.pack(side = "left")
entry_yld = Entry(window)
entry_yld.pack(side = "left")
button_yld = Button(window,
                        text = "Submit Yield",
                        command = get_yield)
button_yld.pack(side = "left")



### Main Loop ###
window.mainloop()