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


reg.fit(list_h,list_w)
m=reg.coef_[0]
b=reg.intercept_

print("slope=",m, "intercept=",b)
ans=reg.predict(X=5.8)
print(ans)

