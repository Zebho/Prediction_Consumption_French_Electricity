
import pandas as pd
import numpy as np

from vacances_scolaires_france import SchoolHolidayDates
from jours_feries_france import JoursFeries


###### Add Columns #######

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

def add_public_holidays(df):
    res_total = {}
    for annee in range(2021,2025):
        res = JoursFeries.for_year(annee)
        res_total.update({f"{cle} {annee}": date for cle, date in res.items()})
    df['public_holiday'] = df['date_hour'].map(lambda x : 1 if (x.date() in res_total.values()) else 0)
    return df


###### Circular Variables  #######

def set_time_columuns(df_final):
    '''
    Création de colonnes heure et minute depuis l'horodate
    Puis suppression des colonnes inutiles (Date, Heures et date_hour)
    '''
    df_final['hour'] = df_final['date_hour'].map(lambda x: x.hour)
    df_final['minute'] = df_final['date_hour'].map(lambda x: x.minute)
    #df_final.drop(columns='date_hour',inplace=True)
    df_final.drop(columns='Date',inplace=True)
    df_final.drop(columns='Heures',inplace=True)
    return df_final

def sin_cos_colonne(df,names_columns):
    df_f = df.copy()
    for name in names_columns:
        df_f[f"sin_{name}"] = df[f"{name}"].apply(lambda h: np.sin(2 * np.pi * h / np.max(df[f"{name}"])))
        df_f[f"cos_{name}"] = df[f"{name}"].apply(lambda h: np.cos(2 * np.pi * h / np.max(df[f"{name}"])))
        df_f.drop([f"{name}"], axis=1, inplace=True)
    return(df_f)

###### Lagged Variables  #######

def shit_colonne(df,names_columns,lagged = [0]):
    if len(names_columns) != len(lagged):
        return("Les listes ne font pas la même taille")
    else:
        df_f = df.copy()
        for index,name in enumerate(names_columns) :
            for i in range(1, lagged[index]+1):
                df_f[f'{name}_shift{i}'] = df_f[f"{name}"].shift(i)
        return df_f.dropna()
