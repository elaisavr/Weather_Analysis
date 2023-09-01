import pandas as pd
import numpy as np
import requests
import datetime
import sys
from datetime import date

# 1) create current end date for analysis time range
tday = datetime.datetime.now()

# 2) create the months list
months = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre','Ottobre','Novembre','Dicembre']

# 3) create a list of years
time_range = pd.date_range(end=tday, periods = 20, freq='A').strftime('%Y').tolist()
# print(time_range)

# 4) cast years to string
years =[]
for i in time_range:
    str(i)
    years.append(i)
# print(years)

# 5) concatenate the end point with every year and month for the analysis, in order to get the datas
endpoint = 'https://www.ilmeteo.it/portale/archivio-meteo/Verona/'
url_list = []
for y in years:
    url_y = y+'/'
    for m in months:
        url_m= url_y+m+'?format=csv'
        url_list.append(url_m)
# print(url_list)

urls = []
for u in url_list:
    ep=endpoint+u
    urls.append(ep)
# print(urls)

# 6) get the datas
weather_list = []
for i in urls:
    url = requests.get(i)
    datas = url.text
    weather_list.append(datas)
# print(weather_list)

# 7) concat the elements into a single string
sep= ',' 
data_string = sep.join(weather_list)
# print(data_string)

# 8) create the DataFrame by splitting the data_string into rows and columns with list comprehension
df = pd.DataFrame([col.split(';') for col in data_string.split('\r\n')])
# print(df)

# 9) switch the columns indexes with the first row containing the headers
df.columns = df.iloc[0].tolist()
# print(df)

# 10) drop the rows where the headers are repeated
df.drop_duplicates(subset='DATA', inplace=True)

# 11) reset the indexes of the records from 0
df = df[1:].reset_index(drop=True)
# print(df)

# 12) save the df into a csv file for the Data Cleaning 
file = df.to_csv('Weather_raw df.csv')

sys.exit()

# --- THE FOLLOWING IS THE DRAFT CODE OF A SINGLE DATA REQUEST ---

#https://www.ilmeteo.it/portale/archivio-meteo/Verona/2023/Agosto?format=csv
#https://www.ilmeteo.it/portale/archivio-meteo/Verona/2000/Gennaio?format=csv

url = 'https://www.ilmeteo.it/portale/archivio-meteo/Verona/2023/Agosto?format=csv'

r = requests.get(url)
print(r.status_code)

#get the text of the url which is the text of a csv file with cell separator ';' and newline '\r\n'
aug_23 = r.text
print(aug_23)
dmeteo = pd.DataFrame([col.split(';') for col in aug_23.split('\r\n')])

#reset the columns indexes with the first raw texts excluding '0' default index with .tolist() method
dmeteo.columns=dmeteo.iloc[0].tolist()

#reset all the indexes from 0, starting from the record with index '1'
dmeteo=dmeteo.iloc[1:]
dmeteo.set_index(pd.RangeIndex(len(dmeteo.iloc[0:])), inplace=True)
print(dmeteo)


