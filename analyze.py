# -*- coding: utf-8 -*-
#!/usr/bin/Anaconda/

"""
1. Ip attempting to login unsuccesfully, might be with different user names
2. Same user name, different passwords coming from different IP's

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.stdout=open('tmp.txt', "w")

data=pd.read_csv("ftp-packets-real.csv")
#initial columns
#frame.number,frame.time,ip.src,ip.dst,_ws.col.Protocol,_ws.col.Info
data.columns=["No","Time","Source","Destination","Protocol","Info"]

invalid_log=data[data["Info"]=="Response: 530 Login or password incorrect!"].copy()
invalid_log['Destination'].fillna("Empty destination IP:Prolly on loopback", inplace=True)
size=len(invalid_log)
if size>0:
    df1 = invalid_log
    df1=df1[df1['Destination'].map(df1['Destination'].value_counts()) > 3]
    df1=df1.drop("No", axis=1)
    df1=df1.drop("Time", axis=1)
    indexes=list(df1.drop_duplicates(keep='last').index)
    invalid_login=invalid_log.loc[indexes,["Time","Destination", "Info"]]
    no_ips=len(invalid_login)
    if no_ips>0:
        invalid_login.reset_index(inplace=True, drop=True)
        print(invalid_login.to_string())



