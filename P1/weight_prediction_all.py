__author__ = 'Nahian'


from matplotlib import pyplot
import csv
from sklearn import linear_model
reg=linear_model.LinearRegression()
X=float(input("Enter Your Height : "))
Y=input("Enter Your Gender :  ")
pound=2.40
list_h=[]
list_w=[]
if Y == "male":
    reg=linear_model.LinearRegression()
    with open("weight-height.csv") as csvfile:

        read=csv.DictReader(csvfile)
        i=0
        for row in read:
           i=i+1
           if i < 5001:
               list_h.append([float(row['Height'])/12])
               list_w.append(float(row['Weight'])/pound)
           else:
               break


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


if Y == "female":
    reg=linear_model.LinearRegression()

    with open("weight-height.csv") as csvfile:

        read=csv.DictReader(csvfile)
        i=0
        for row in read:
           i=i+1
           if i < 5001:
               continue


           else:
                 list_h.append([float(row['Height'])/12])
                 list_w.append(float(row['Weight'])/pound)



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





