__author__ = 'Nahian'

from matplotlib import pyplot
import csv
from sklearn import linear_model
reg=linear_model.LinearRegression()
list_h=[]
list_w=[]
with open("weight-height.csv") as csvfile:
    read=csv.DictReader(csvfile)
    for row in read:
        list_h.append([float(row['Height'])/12])
        list_w.append(float(row['Weight'])/2.5)
x=[5,6,7,8]
y=[7,3,8,3]
pyplot.plot(list_h,list_w)
pyplot.title("History of sales")
pyplot.xlabel("X axis")
pyplot.ylabel("Y axis")
pyplot.show()

