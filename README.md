# ML_Predict_Weight_Over_Height
INTRODUCTION: 
In our project our goal is to predict height and weight by using machine learning. Linear approach for modeling the relationship between a scalar dependent variable Y and one or more explanatory variables denoted X. we collect thousands of data and we perform linear regression and by using equation of straight line(Y=mx + c)  we showed the graph of  expected outcome .
BACKGROUND
Steps involved in weight prediction used in this paper are:
	Random Height & weight of n human (Suitable solutions).
	Find slope & intercept from database.
	Apply regression with given input to predict weight.

Requirements Specification
	Simple linear regression: it concerns two-dimensional sample points with one independent variable and one dependent variable (conventionally, the x and y coordinates in a Cartesian coordinate system) and finds a linear function (a non-vertical straight line) that, as accurately as possible, predicts the dependent variable values as a function of the independent variables. The adjective simple refers to the fact that the outcome variable is related to a single predictor.								
 

 
The first graph is for positive relation. Where the value of slope will always be positive.
y=mx+c
The second graph is for negative relation where the value of slope will always be negative.
y=-mx+c
In our project height-weight relation is positive .So our linear regression will be positive.
Output consists of more than one continuous variables, then the task is called regression.

Necessary tools:
	Python3;
	Pip3;
	Numpy;
	Sk-learn;
	Mathpotlib.

Python contain special libraries for machine learning namely scipy and numpy which great for linear algebra and getting to know kernel methods of machine learning. NumPy's arrays are more compact than Python lists. in Python, would take at least 20 MB or so, while a NumPy 3D array with single-precision floats in the cells would fit in 4 MB. Access in reading and writing items is also faster with NumPy. scikit-learn  used for Loading an example dataset, Learning and predicting , Choosing the parameters of the model for machine learning.


	Use Case Diagram and Description
IMPLEMENTATION

Data Collection & process 
Gender	Height(inch)	Weight(pound)
Male	67.40000	194.0000653
Male	72.87643	188.0654316
Female	66.87654	173.9863256

Fig 1: Data-training-set of population.
In our database we collect nearly thousand data of male and female. We didn’t classified our data so we collect both genders data in a single database and performed general regression.
 
                                                                                       Process









Fig 3: Prediction Process.

	The database will be the population.
	Using numpy all data will be in two separate array (height & weight).
	Linear regression will be applied on arrays to get slope and intercept.
	Predicted weight will get from the result of Y.

Units
Initially height is in inch and weight is in pound.
User’s input will be in feet.
Data set will be stored using numpy as feet & kg units.
Final result will be displayed in a graph.

Equations

Weight =slope*height + intercept.





RESULT

  

 



