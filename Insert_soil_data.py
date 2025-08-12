import pandas as pd

def insert_data(plot_id,clay,p,k,ctc,v,ca,mg):
    csv = pd.read_csv("Soil_Analysis.csv")
    csv.loc[len(csv)] = [plot_id,clay,p,k,ctc,v,ca,mg]
    csv.to_csv("Soil_Analysis.csv",index = False)
    return print(csv)
