import random
import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

dataSet = []
def randomSet(counter):
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data))
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

mean = statistics.mean(dataSet)

meanList = []
for i in range(0, 1000):
    setMean = randomSet(100)
    meanList.append(setMean)
std_deviation = statistics.stdev(meanList)
mean2 = statistics.mean(meanList)
print("Std_dev is:", std_deviation )
print("Mean is:", mean)

z_score = (mean-mean2)/std_deviation
print("z score:", z_score)