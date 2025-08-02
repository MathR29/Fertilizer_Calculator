import pandas as pd

class Soil:
    p_deficit = 0
    k_deficit = 0
    mg_deficit = 0
    ca_deficit = 0
    CTC = 0
    V = 0
    Phosphorus = 0
    Potassium = 0
    Calcium = 0
    Magnesium = 0
    Clay = 0

    def __init__(self,plot_id):
        self.populate_info("Soil_Analysis.csv",plot_id)
        self.deficits()

    def populate_info(self,path,plot_id):
        csv = pd.read_csv(path)
        df_soil = csv[csv["plot_id"] == plot_id]
        self.CTC = df_soil["ctc"].values[0]
        self.V = df_soil["v"].values[0]
        self.Phosphorus = df_soil["p"].values[0]
        self.Potassium = df_soil["k"].values[0]
        self.Calcium = df_soil["ca"].values[0]
        self.Magnesium = df_soil["mg"].values[0]
        self.Clay = df_soil["clay"].values[0]


    def deficits(self):
        if self.Clay < 25:
            self.p_deficit = 18 - self.Phosphorus if self.Phosphorus < 18 else 0

        elif 25 <= self.Clay < 40:
            self.p_deficit = 12 - self.Phosphorus if self.Phosphorus < 12 else 0

        else:
            self.p_deficit = 9 - self.Phosphorus if self.Phosphorus < 9 else 0

        self.k_deficit = 0.21 - self.Potassium if self.Potassium < 0.21 else 0
        self.ca_deficit = 2 - self.Calcium if self.Calcium < 2 else 0
        self.mg_deficit = 1 - self.Magnesium if self.Magnesium < 1 else 0

        return {
            "P_Deficit": round(self.p_deficit,2),
            "K_Deficit": round(self.k_deficit,2),
            "Ca_Deficit": round(self.ca_deficit,2),
            "Mg_Deficit": round(self.mg_deficit,2)
        }


class Crop:
    name = ""
    n_upk = 0
    p_upk = 0
    k_upk = 0
    v_max = 0
    v_min = 0 #V == Saturação por bases
    yld = 0

    def __init__(self,name,n_upk,p_upk,k_upk,v_max,v_min,yld):
        self.name = name
        self.yld = yld
        self.n_upk = n_upk
        self.p_upk = p_upk
        self.k_upk = k_upk
        self.v_max = v_max
        self.v_min = v_min  

    def nutrients_required(self):
        n_total = round(self.n_upk * self.yld, 2)
        p_total = round(self.p_upk * self.yld * 2.29, 2)
        k_total = round(self.k_upk * self.yld * 1.20458, 2)
        return{
            'N': round(n_total,2),
            'P': round(p_total,2),
            'K': round(k_total,2)
        }

class Corn(Crop):
    def __init__(self,yld):
        super().__init__("Corn",
                         n_upk = 14.4,
                         p_upk = 3.4,
                         k_upk = 5.4,
                         v_min = 60,
                         v_max = 70,
                         yld = yld)

class Wheat(Crop):
    def __init__(self,yld):
        super().__init__("Wheat",
                         n_upk = 20,
                         p_upk = 3.2,
                         k_upk = 3.5,
                         v_min = 60,
                         v_max = 70,
                         yld = yld)

class Soybean(Crop):
    def __init__(self,yld):
        super().__init__("Soybean",
                         n_upk = 0,
                         p_upk = 4.5,
                         k_upk = 14.2,
                         v_min = 50,
                         v_max = 60,
                         yld = yld)

class FertCalc:

    @staticmethod
    def correction_fertilization(soil):
        p_correction = soil.p_deficit * 2 * 2.29 # P2O5
        k_correction = soil.k_deficit * 391 * 2 * 1.20458 # K2O
        ca_correction = soil.ca_deficit * 200.4 * 2 * 1.4 # CaO
        mg_correction = soil.mg_deficit * 121.56 * 2 * 1.67 # MgO

        return {
            "P_correction": round(p_correction,2),
            "K_correction": round(k_correction,2),
            "Ca_correction": round(ca_correction,2),
            "Mg_correction": round(mg_correction,2)
        }

    @staticmethod
    def maintenance_fertilization(crop):
        n_maintenance = crop.n_upk * crop.yld
        p_maintenance = crop.p_upk * crop.yld
        k_maintenance = crop.k_upk * crop.yld

        return {
            "N_maintenance": round(n_maintenance,2),
            "P_maintenance": round(p_maintenance,2),
            "K_maintenance": round(k_maintenance,2)
        }

    @staticmethod
    def total_fertilization(correction,maintenance):
        n = maintenance['N_maintenance']
        p = maintenance['P_maintenance'] + correction['P_correction']
        k = maintenance['K_maintenance'] + correction['K_correction']

        return {
            "N": round(n,2),
            "P": round(p,2),
            "K": round(k,2)
        }
    @staticmethod
    def lime_required(crop,soil):
        lime_required = round(((crop.v_max - soil.V) * soil.CTC)/100,2)
        return lime_required
