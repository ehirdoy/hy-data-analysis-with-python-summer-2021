#!/usr/bin/env python3

import pandas as pd

weekdays = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

def bicycle_timeseries():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)

    p = df.Päivämäärä.str.split(expand=True)
    p.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    p.Hour = p.Hour.str.split(':', expand=True)[0]
    p.Weekday, p.Month = p.Weekday.map(weekdays), p.Month.map(months)
    p = p.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    p["Date"] = pd.to_datetime(p[["Year", "Month", "Day", "Hour"]])
    df = pd.concat([p, df.iloc[:,1:]], axis=1)
    df.index = df.Date
    df = df.drop(["Date", "Day", "Month", "Year", "Hour", "Weekday"], axis=1)
    return df


def main():
    print(bicycle_timeseries())

if __name__ == "__main__":
    main()
