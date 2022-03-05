import numpy as np
import pandas as pd
Number_of_courses= int(input("Number of courses:"))
i= 0
def Values():
	if number <= 39:
		data['values'].append(0)
	elif number >=40 and number<=44:
		data['values'].append(1)
	elif number >=45 and number <=49:
		data['values'].append(2)
	elif number>=50 and number<=59:
		data['values'].append(3)
	elif number>=60 and number<=69:
		data['values'].append(4)
	elif number>=70 and number<=100:
		data['values'].append(5)
data={
		'courses': [],
		'units':[],
		'scores':[],
		'values':[]
}
while Number_of_courses != i:
	course= input("Enter a course:")
	data['courses'].append(course)
	units=int(input("Enter the units of the course:"))
	data['units'].append(units)
	scores=int(input("Enter your score:"))
	data['scores'].append(scores)
	i+=1
for number in data['scores']:
	Values()
df= pd.DataFrame(data)
print(df)
sum_of_units=df['units'].sum()
values_times_units = df['values']*df['units']
Sum= values_times_units.sum()
Average= Sum/sum_of_units
Average_2sf= "{:.2f}".format(Average)
print("cgpa=",Average_2sf)

