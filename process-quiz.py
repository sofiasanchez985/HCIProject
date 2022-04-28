import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def summary(df):
    chartDF = pd.DataFrame(columns=["total","extreme", "numeric", "fact"])
    chartDF['total'] = df.sum(axis=1) / 30
    chartDF['extreme'] = df.iloc[:,0:10].sum(axis=1) / 10
    chartDF['numeric'] = df.iloc[:,10:20].sum(axis=1) / 10
    chartDF['fact'] = df.iloc[:,20:30].sum(axis=1) / 10

    total_mean = np.mean(chartDF['total'])
    extreme_mean = np.mean(chartDF['extreme'])
    numeric_mean = np.mean(chartDF['numeric'])
    fact_mean = np.mean(chartDF['fact'])

    total_std = np.std(chartDF['total'])
    extreme_std = np.std(chartDF['extreme'])
    numeric_std = np.std(chartDF['numeric'])
    fact_std = np.std(chartDF['fact'])
    
    return pd.DataFrame(np.array([[total_mean,extreme_mean,numeric_mean,fact_mean,total_std,extreme_std,numeric_std,fact_std],]), columns=["total_mean","extreme_mean","numeric_mean","fact_mean","total_std","extreme_std","numeric_std","fact_std"])

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

stat = summary(score2D)
stat = stat.append(summary(scoreAR))
stat["type"] = ["2D","AR"]
print(stat)

# chart = pd.DataFrame(columns=summary2D.columns, index=[0,1])
# for i in range(len(chart.columns)):
#     if chart.columns[i] == "total":
#         p = np.sum(summaryAR[chart.columns[i]])/
#         chart.iloc[0,i] = p
#     else:
#         p = np.sum(summaryAR[chart.columns[i]])/90
#         chart.iloc[0,i] = p

# for i in range(len(chart.columns)):
#     if chart.columns[i] == "total":
#         p = np.sum(summary2D[chart.columns[i]])/270
#         chart.iloc[1,i] = p
#     else:
#         p = np.sum(summary2D[chart.columns[i]])/90
#         chart.iloc[1,i] = p

# chart["type"] = ["AR","2D"]
# print(chart)

score2D_summary = summary(score2D).iloc[0]
scoreAR_summary = summary(scoreAR).iloc[0]


values = ['Total', 'Extreme', 'Numeric', 'Facts']
x_pos = 10 * np.arange(len(values))
SCORES_2D = [score2D_summary['total_mean'], score2D_summary['extreme_mean'], score2D_summary['numeric_mean'], score2D_summary['fact_mean']]
error_2D = [score2D_summary['total_std'], score2D_summary['extreme_std'], score2D_summary['numeric_std'], score2D_summary['fact_std']]

SCORES_AR = [scoreAR_summary['total_mean'], scoreAR_summary['extreme_mean'], scoreAR_summary['numeric_mean'], scoreAR_summary['fact_mean']]
error_AR = [scoreAR_summary['total_std'], scoreAR_summary['extreme_std'], scoreAR_summary['numeric_std'], scoreAR_summary['fact_std']]


# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos-2, SCORES_2D, width=4, yerr=error_2D, align='center', alpha=0.5, ecolor='black', capsize=2, label='2D')
ax.bar(x_pos+2, SCORES_AR, width=4, yerr=error_AR, align='center', alpha=0.5, ecolor='black', capsize=2, label='AR')

ax.set_ylabel('Scores')
ax.set_xticks(x_pos)
ax.set_xticklabels(values)
ax.set_title('Scores')
ax.legend()
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()


print(summary(score2D).iloc[0]['total_mean'])

