__author__ = 'Nahian'
from matplotlib import pyplot
import csv
from sklearn import linear_model
reg=linear_model.LinearRegression()
list_h=[]
list_w=[]
X=float(input("Enter Your Height :"))

with open("class_data.csv") as csvfile:
    read=csv.DictReader(csvfile)
    i=0
    for row in read:
        list_h.append([float(row['height'])])
        list_w.append(float(row['weight']))


reg.fit(list_h,list_w)
m=reg.coef_[0]
b=reg.intercept_

print("slope=",m, "intercept=",b)
ans=reg.predict(X)
print(ans)

pyplot.plot(list_h,list_w,'ro')
pyplot.plot(X,ans,'bs')
pyplot.title("height and weight")
pyplot.xlabel("X axis")
pyplot.ylabel("Y axis")
pyplot.show()