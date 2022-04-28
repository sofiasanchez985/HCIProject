import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def summary(df):
    chartDF = pd.DataFrame(columns=["total","extreme", "numeric", "fact"])
    chartDF['total'] = df.sum(axis=1)
    chartDF['extreme'] = df.iloc[:,0:10].sum(axis=1)
    chartDF['numeric'] = df.iloc[:,10:20].sum(axis=1)
    chartDF['fact'] = df.iloc[:,20:30].sum(axis=1) 

    return chartDF

def checkAns(type):
    input = pd.read_csv( type+".csv", sep = ",", header=1, index_col="Participant ID")
    input = input.drop('Participant Name', axis=1)
    directory = 'ans/'+ type

    scoreDF = pd.DataFrame(columns=input.columns, index=range(1,10))

    # iterate over files in directory
    for i in range(1,10):
        filename = directory + "/answers_" + type + "_" + str(i) + ".txt"
        if (os.path.exists(filename)):
            answers = input.loc[i]
            with open(filename, "r") as f:
                text = f.readlines()
                extreme = text[2:12]
                others = text[15:25]+text[28:38]
                for j in range(len(extreme)):
                    extreme[j] = extreme[j].strip()
                    answer = extreme[j][-1]
                    if(answer == answers[j]):
                        scoreDF.iloc[i-1,j] = 1
                    else:
                        scoreDF.iloc[i-1,j] = 0
                for j in range(len(others)):
                    answer = others[j][0]
                    if(answer == answers[j+10]):
                        scoreDF.iloc[i-1,j+10] = 1
                    else:
                        scoreDF.iloc[i-1,j+10] = 0
    scoreDF.to_csv(type+"scores.csv", sep=",")
    return scoreDF

score2D = checkAns("2D")
scoreAR = checkAns("AR")

summary2D = summary(score2D)
summaryAR = summary(scoreAR)

chart = pd.DataFrame(columns=summary2D.columns)
for col in chart.columns:
    if col == "total":
        p = np.sum(summaryAR[col])/30
    else:
        p = np.sum(summaryAR[col])/10
        chart[col].append(p)
print(chart)
