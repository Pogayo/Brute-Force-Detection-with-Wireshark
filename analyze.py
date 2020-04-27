# -*- coding: utf-8 -*-
#!/usr/bin/Anaconda/

"""
1. Ip attempting to login unsuccesfully, might be with different user names
2. Same user name, different passwords coming from different IP's
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("ftp-packets.csv")

invalid_log=data[data["Info"]=="Response: 530 Login or password incorrect!"]

df1 = invalid_log[invalid_log['Source'].map(invalid_log['Source'].value_counts()) > 3]
df1=df1.drop("No.", axis=1)
df1=df1.drop("Time", axis=1)

indexes=list(df1.drop_duplicates(keep='last').index)
invalid_login=invalid_log.loc[indexes,["Time","Destination", "Info"]]
no_ips=len(invalid_login)

invalid_login.reset_index(inplace=True, drop=True)

message="Dear Admin,\n \n"+str(no_ips) +" ip addresses have tried loggin in more than 3 times. Find details below."
print(message)
print(invalid_login.to_string())
print("\nBest regards,\nThe Powershell script you wrote")

