import os.path
from numpy import ndarray
import pandas as pd
import numpy as np
 
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
                        scoreDF.iloc[i,j] = 1
                    else:
                        scoreDF.iloc[i,j] = 0
    print(scoreDF)



checkAns("2D")