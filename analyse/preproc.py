import pandas as pd
import numpy as np

####### Preprocessing Data ############
def preprocessing_RTE_encours(df):
    '''
    This preprocessing in on the file "RTE eCO2mix_RTE_En-cours-TR.csv"
    '''
    colum_keep = ['Date', 'Heures','Consommation']#,'Prévision J-1']

    df.reset_index(inplace=True)
    df.columns = ['Périmètre', 'Nature', 'Date', 'Heures', 'Consommation',
        'Prévision J-1', 'Prévision J', 'Fioul', 'Charbon', 'Gaz', 'Nucléaire',
        'Eolien', 'Solaire', 'Hydraulique', 'Pompage', 'Bioénergies',
        'Ech. physiques', 'Taux de Co2', 'Ech. comm. Angleterre',
        'Ech. comm. Espagne', 'Ech. comm. Italie', 'Ech. comm. Suisse',
        'Ech. comm. Allemagne-Belgique', 'Fioul - TAC', 'Fioul - Cogén.',
        'Fioul - Autres', 'Gaz - TAC', 'Gaz - Cogén.', 'Gaz - CCG',
        'Gaz - Autres', 'Hydraulique - Fil de l?eau + éclusée',
        'Hydraulique - Lacs', 'Hydraulique - STEP turbinage',
        'Bioénergies - Déchets', 'Bioénergies - Biomasse',
        'Bioénergies - Biogaz', ' Stockage batterie', 'Déstockage batterie',
        'Eolien terrestre', 'Eolien offshore','extra']
    df.drop(columns='extra',inplace=True)

    df.drop(df.tail(1).index,inplace = True) #On enlève la dernière ligne ajouté par RTE
    df_final = df[colum_keep]
    df_final['date_hour'] = pd.to_datetime(df_final['Date']+ " " + df_final['Heures'])
    df_final['Date'] = pd.to_datetime(df_final['Date'])
    df_final['Heures'] = df_final['date_hour'].map(lambda x : x.time())

    #df_final['Prévision J-1'] = pd.to_numeric(df_final['Prévision J-1'],errors='coerce')
    #df_final['Prévision J-1'].interpolate(method='linear',limit_direction='both',inplace=True)

    df_final.dropna(inplace=True)
    return df_final[[ 'Date', 'Heures', 'date_hour','Consommation']]#'Prévision J-1']]

def preproc_temperature_ENEDIS(df):
    '''
    This preprocessing in on the file about temperatur eof ENEDIS

    '''
    colum_temp = ['horodate', 'temperature_realisee_lissee_degc',
                  'annee', 'mois', 'jour', 'annee_mois_jour']
    df_reduced = df[colum_temp]
    df_reduced['horodate'] = df_reduced['horodate'].map(lambda x : x[:-6])
    df_reduced['horodate'] = pd.to_datetime(df_reduced['horodate'],utc=False)
    df_reduced.drop(columns='annee_mois_jour',inplace=True)
    df_reduced.sort_values(by='horodate',inplace=True)
    df_reduced.columns = ['date_hour', 'temperature_realisee_lissee_degc', 'annee', 'mois',
       'jour']
    return df_reduced

def preproc_tempo(df_TEMPO_annee_n):
    '''
    This preprocessing in on the file "TEMPO" of ECO2Mix
    '''

    df_TEMPO_annee_n.drop(df_TEMPO_annee_n.tail(1).index,inplace = True)
    df_TEMPO_annee_n['Date'] = pd.to_datetime(df_TEMPO_annee_n['Date'], format="%Y-%m-%d")
    return df_TEMPO_annee_n
