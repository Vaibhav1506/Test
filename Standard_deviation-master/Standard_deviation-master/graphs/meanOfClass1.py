import csv

from plotly import graph_objs

with open('class1.csv', newline='') as file:
    reader= csv.reader(file)
    fileData = list(reader)

fileData.pop(0) 

totalMarks = 0
n = len(fileData)

for i in fileData:
    totalMarks += float(i[1])

mean = totalMarks/n

print("The mean of the marks is" + str(mean))

import pandas as pd
import plotly.express as px

f = pd.read_csv('class1.csv')

fig = px.scatter(f, x = "Student Number", y = "Marks")

fig.update_layout(shapes=[
    dict(
        type = "line",
        y0 = mean, y1 = mean,
        x0 = 0, x1 = n
    )
])

fig.update_yaxes(rangeMode = "tozero")

fig.show()
