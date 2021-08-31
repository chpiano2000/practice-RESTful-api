import requests
import pdb
from datetime import datetime
import pandas as pd

def weather(q, appid, units):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={q}&appid={appid}&units={units}'
    data = requests.get(url).json()

    # pre-processing data
    lists1 = []
    lists2 = []
    for i in data["list"]:
        lists1.append(i["dt"])
        lists2.append(datetime.fromtimestamp(i["dt"]).day)
        final = []
    
    df = pd.DataFrame(lists1)
    df.columns = ['unix']
    df['day'] = lists2

    df = df.groupby(df['day']).min()
    result = df['unix'].tolist()
    
    # lists of final data
    final = []
    for i in data["list"]:
        if i['dt'] in result:
            model = {
                "day": datetime.fromtimestamp(i["dt"]).strftime('%A'),
                "main": i["weather"][0]["main"],
                "temp": round(i["main"]["temp"] - 273.15, 2),
                "visibility": i["visibility"] / 1000
            }
            final.append(model)
        
    return final