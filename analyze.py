# -*- coding: utf-8 -*-
#!/usr/bin/Anaconda/

"""

"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("ftp-packets.csv")

invalid_log=data[data["Info"]=="Response: 530 Login or password incorrect!"]

counts=invalid_log.Destination.value_counts()
no_ips=len(counts)

invalid_login=invalid_log[["Time","Destination"]]

invalid_login.reset_index(inplace=True, drop=True)

message="Dear Admin,\n \n"+str(no_ips) +" ip addresses have tried loggin in more than 3 times. Find details below."
print(message)
print(invalid_login)
print("\nBest regards,\nThe Powershell script you wrote")

