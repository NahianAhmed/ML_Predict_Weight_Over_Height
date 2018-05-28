__author__ = 'Nahian'
from sklearn import linear_model
from matplotlib import pyplot

height=[[4.0],[4.5],[5.0],[5.2],[5.4],[5.8],[6.1],[6.2],[6.4],[6.8]]
weight=[  42 ,  44 , 49, 55  , 53  , 58   , 60  , 64  ,  66 ,  69]

#print("height weight")
#for row in zip(height, weight):
  #  print(row[0][0],"->",row[1])

reg=linear_model.LinearRegression()
reg.fit(height,weight)
m=reg.coef_[0]
b=reg.intercept_
X=5.8
ans=reg.predict(X)
print("slope=",m, "intercept=",b)
print(ans)
pyplot.plot(height,weight,"bs")
pyplot.plot(X,ans,'ro')
pyplot.title("History of sales")
pyplot.xlabel("X axis")
pyplot.ylabel("Y axis")
pyplot.show()


