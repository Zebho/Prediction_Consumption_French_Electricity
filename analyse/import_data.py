import pandas as pd

def import_TEMPO(racine = 'data/puissance/',deb=2021,fin=2023):
    TEMPO_all = {}
    for k in range(deb,fin+1):
        try :
            TEMPO_all[f'eCO2mix_RTE_tempo_{k}-{k+1}'] = pd.read_csv(f"{racine}eCO2mix_RTE_tempo_{k}-{k+1}.csv",delimiter=";")
        except:
            print(f"Le document eCO2mix_RTE_tempo_{k}-{k+1} n est pas à la racine {racine}")
    return TEMPO_all
