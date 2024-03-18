import pandas as pd
import requests
import zipfile
from colorama import Fore, Style
from pathlib import Path

def import_TEMPO(racine = 'data_raw/tempo/',deb=21,fin=23):
    TEMPO_all = {}

    for k in range(deb,fin+1):
        cache_path = cache_path = Path("data_raw").joinpath("tempo",f"eCO2mix_RTE_tempo_20{k}-20{k+1}.xls")
        if cache_path.is_file():
            print(Fore.BLUE + f"\nLoad data 20{k}-20{k+1} from  local CSV..." + Style.RESET_ALL)
            try :
                TEMPO_all[f'eCO2mix_RTE_tempo_20{k}-20{k+1}'] = pd.read_csv(f"{racine}eCO2mix_RTE_tempo_20{k}-20{k+1}.xls",encoding = "ISO-8859-1", delimiter='\t')
            except:
                print(f"Le document eCO2mix_RTE_tempo_20{k}-20{k+1} n est pas à la racine {racine}")
        else:
            print(f"TEMPO data retrieval year 20{k}-20{k+1} online")
            try :
                #Retrieve the most recent data from the RTE website
                URL = f"https://eco2mix.rte-france.com/curves/downloadCalendrierTempo?season={k}-{k+1}"
                response = requests.get(URL)
            except:
                return(f"The file is not availaible at the url {URL}")
            open(f"data_raw/tempo/eCO2mix_RTE_tempo_20{k}-20{k+1}.zip", "wb").write(response.content)

            #DeZipping process
            myZip = zipfile.ZipFile(f"data_raw/tempo/eCO2mix_RTE_tempo_20{k}-20{k+1}.zip")
            myZip.extractall(f"data_raw/tempo/")

            try :
                TEMPO_all[f'eCO2mix_RTE_tempo_20{k}-20{k+1}'] = pd.read_csv(f"{racine}eCO2mix_RTE_tempo_20{k}-20{k+1}.xls",encoding = "ISO-8859-1", delimiter='\t')
            except:
                print(f"Le document eCO2mix_RTE_tempo_20{k}-20{k+1} n est pas à la racine {racine}")

    return TEMPO_all

def import_RTE_TR():
    #request each time online because update every day
    print("RTE Data Retrieval online")
    try :
        #Retrieve the most recent data from the RTE website
        URL = "https://eco2mix.rte-france.com/download/eco2mix/eCO2mix_RTE_En-cours-TR.zip"
        response = requests.get(URL)
    except:
        return(f"The file is not availaible at the url {URL}")
    open("data_raw/eCO2mix_RTE_En-cours-TR.zip", "wb").write(response.content)

    #DeZipping process
    myZip = zipfile.ZipFile("data_raw/eCO2mix_RTE_En-cours-TR.zip")
    myZip.extractall('data_raw/')

    #Reading and creating the new dataframe in pandas
    df = pd.read_csv('data_raw/eCO2mix_RTE_En-cours-TR.xls',encoding = "ISO-8859-1", delimiter='\t')

    return df

def import_temp_ENEDIS():
    cache_path = Path("data_raw").joinpath("donnees-de-temperature-et-de-pseudo-rayonnement.csv")
    if cache_path.is_file():
        print(Fore.BLUE + f"\nLoad data from local CSV..." + Style.RESET_ALL)
        try :
            df = pd.read_csv('data_raw/donnees-de-temperature-et-de-pseudo-rayonnement.csv',encoding = "utf-8", delimiter=';')
        except:
            print(f"Le document enedis n est pas à la racine")
    else:
        print("ENEDIS Data Retrieval online")
        try :
            #Retrieve the most recent data from the RTE website
            URL = "https://www.data.gouv.fr/fr/datasets/r/7ebeddda-dd11-488f-9092-10a1915a3fcd"
            response = requests.get(URL)
        except:
            return(f"The file is not availaible at the url {URL}")
        open("data_raw/donnees-de-temperature-et-de-pseudo-rayonnement.csv", "wb").write(response.content)

        #Reading and creating the new dataframe in pandas
        df = pd.read_csv('data_raw/donnees-de-temperature-et-de-pseudo-rayonnement.csv',encoding = "utf-8", delimiter=';')
    return df
