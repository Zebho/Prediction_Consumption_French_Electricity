import pandas as pd
from vacances_scolaires_france import SchoolHolidayDates
from jours_feries_france import JoursFeries

import numpy as np


def preprocessing_RTE_encours(df):
    '''
    A faire sur le fichier RTE eCO2mix_RTE_En-cours-TR.csv
    '''
    colum_keep = ['Date', 'Heures','Consommation']#,'Prévision J-1']

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
    A appliquer sur importation de

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

def add_weekday(df):
    '''
    A appliquer sur un df avec 'date_hour' en datetime
    '''
    df['weekday'] = df['date_hour'].map(lambda x : x.weekday())
    return df

def add_schoolholidays(df):
    '''
    A appliquer sur un df avec 'date_hour' en datetime
    Sortie : entré + colonne
    '''
    d = SchoolHolidayDates()
    df['school_holiday'] = df['date_hour'].map(lambda x : 1 if d.is_holiday(x.date()) else 0)
    return df

def preproc_tempo(df_TEMPO_annee_n):
    '''
    Pas de modif sur le fichier TEMPO
    '''

    df_TEMPO_annee_n.drop(df_TEMPO_annee_n.tail(1).index,inplace = True)
    df_TEMPO_annee_n['Date'] = pd.to_datetime(df_TEMPO_annee_n['Date'], format="%Y-%m-%d")
    return df_TEMPO_annee_n


def add_public_holidays(df):
    res_total = {}
    for annee in range(2021,2025):
        res = JoursFeries.for_year(annee)
        res_total.update({f"{cle} {annee}": date for cle, date in res.items()})
    df['public_holiday'] = df['date_hour'].map(lambda x : 1 if (x.date() in res_total.values()) else 0)
    return df
