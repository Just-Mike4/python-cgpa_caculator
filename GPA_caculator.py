import numpy as np
import pandas as pd
Number_of_courses= int(input("Number of courses:"))
i= 0
def Points():
	if number <= 39:
		data['points'].append(0)
	elif number >=40 and number<=44:
		data['points'].append(1)
	elif number >=45 and number <=49:
		data['points'].append(2)
	elif number>=50 and number<=59:
		data['points'].append(3)
	elif number>=60 and number<=69:
		data['points'].append(4)
	elif number>=70 and number<=100:
		data['points'].append(5)
def Remark():
	if Average_2sf  <= 1:
		print("Fail")
	elif Average_2sf >= 1 and Average_2sf <= 1.49:
		print("Pass")
	elif Average_2sf >= 1.5 and Average_2sf <=2.39 :
		print ("3rd Class")
	elif Average_2sf >= 2.40 and Average_2sf <= 3.49:
		print("2nd Class Lower")
	elif Average_2sf >= 3.50 and Average_2sf <= 4.49:
		print ("2nd Class Upper")
	elif Average_2sf >= 4.50 and Average_2sf <= 5.00:
		print("First Class")
		
data={
		'courses': [],
		'units':[],
		'scores':[],
		'points':[]
}
while Number_of_courses != i:
	course= input("Enter a course:")
	data['courses'].append(course)
	units=int(input("Enter the units of the course:"))
	data['units'].append(units)
	scores=int(input("Enter your score(/100):"))
	data['scores'].append(scores)
	i+=1
for number in data['scores']:
	Points()
df= pd.DataFrame(data)
print(df)
sum_of_units=df['units'].sum()
Points_times_units = df['points']*df['units']
Sum= Points_times_units.sum()
Average= Sum/sum_of_units
Average_2sf=float("{:.2f}".format(Average))
print("cgpa=",Average_2sf)
Remark()
