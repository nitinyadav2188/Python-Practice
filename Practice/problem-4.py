#to calculate BMI=kg/m square 
weight_in_kg=float(input("Enter weight in kg:"))
height_in_meter=float(input("Enter height in meters:"))
bmi=weight_in_kg/(height_in_meter*height_in_meter)
print("BMI is:",bmi)